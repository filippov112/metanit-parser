from threading import Thread
from os import makedirs, path
from re import sub, compile
from json import dump, load, loads
from asyncio import Semaphore, sleep, gather, run
from urllib.parse import urljoin
from PySide6.QtCore import Signal
from aiohttp import ClientSession
from bs4 import BeautifulSoup
from PySide6.QtWidgets import QFileDialog
from sys import argv, exit
from PySide6.QtWidgets import QApplication, QMainWindow
from form import Ui_MainWindow


class MainWindow(QMainWindow):
    update_log_signal = Signal(str)

    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.running = False
        self.semaphore = Semaphore(5)  # Одновременно не более 5 запросов

        self.ui.q_load.clicked.connect(self.__load_config)
        self.ui.q_save.clicked.connect(self.__save_config)
        self.ui.q_start.clicked.connect(self.__on_start)

        self.update_log_signal.connect(self.__update_log)
        self.__load_config_from()

    def __log_message(self, message):
        self.update_log_signal.emit(message)

    def __update_log(self, message):
        self.ui.log_window.appendPlainText(message)

    async def __fetch_content(self, session: ClientSession, url, selector):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/91.0.4472.124 Safari/537.36'
        }
        try:
            async with self.semaphore:  # Ограничение количества одновременных запросов
                await sleep(1)  # Пауза между запросами
                async with session.get(url, headers=headers) as response:
                    if response.status != 200:
                        self.__log_message(f"Ошибка {response.status} при обращении к {url}")
                        return None
                    soup = BeautifulSoup(await response.text(), 'html.parser')
                    return soup.select(selector)
        except Exception as e:
            self.__log_message(f"Ошибка запроса: {e}")
            return None

    @staticmethod
    def __clean_text(html_content, patterns, replacements, selectors):
        soup = BeautifulSoup(str(html_content), 'html.parser')
        # Фильтруем лишние CSS селекторы
        if selectors:
            for selector in selectors:
                for elem in soup.select(selector):
                    elem.decompose()
        # Разделяем тэги по строкам
        text = str(soup).replace('><', '>\n<')
        # Удаляем квадратные скобки по краям
        if len(text) > 1:
            text = text[1:-1]
        text = text.replace('<pre class="brush:xml;">', ' ').replace('</pre>', ' ')
        # Применяем регулярные выражения замены (удаляем все html-тэги)
        for pattern in patterns:
            text = sub(pattern, '', text)
        # Заменяем фрагменты текста (экранируем угловые скобки в кодовых блоках)
        for old, new in replacements.items():
            text = text.replace(old, new)
        # Удаляем пустые строки
        return '\n'.join(line for line in text.replace('\r\n', '\n').split('\n') if len(line) > 0)

    def __save_content(self, path1, path2, filename, header1, content, footer1, header2, footer2, url, title):
        self.__write_to_file(path1, filename, header1, footer1, content, url, title)
        self.__write_to_file(path2, filename, header2, footer2, "", url, title)
        self.__log_message(f"Файл сохранен: {filename}")

    @staticmethod
    def __write_to_file(dir_path, filename, header, footer, content, url, title):
        makedirs(dir_path, exist_ok=True)
        filepath = path.join(dir_path, filename.replace('/', ' ').replace('\\', ' '))
        header = header.replace("{%link%}", url).replace("{%title%}", title)
        footer = footer.replace("{%link%}", url).replace("{%title%}", title)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(f"{header}\n{content}\n{footer}")

    @staticmethod
    def __clear_filename(text):
        pattern = compile(r'[^a-zA-Zа-яА-ЯёЁ0-9.,\- ]')
        filtered_text = sub(pattern, '', text)
        return filtered_text

    async def __parse(self):
        try:
            self.ui.log_window.clear()

            url = self.ui.entry_url.text()
            single_url = self.ui.entry_url2.text().strip()
            single_name = self.ui.single_file_name.text().strip()

            save_path = self.ui.entry_path.text()
            save_path_2 = self.ui.entry_path2.text()

            header = self.ui.entry_header.toPlainText().strip()
            footer = self.ui.entry_footer.toPlainText().strip()
            h2 = self.ui.header2.toPlainText().strip()
            f2 = self.ui.footer2.toPlainText().strip()

            selectors_content = self.ui.content.text()
            selectors_chapter_block = self.ui.chapter_block.text()
            selectors_chapter_name = self.ui.chapter_name.text()
            selectors_page = self.ui.page.text()

            patterns = self.ui.entry_regex.toPlainText().strip().split('\n')
            filter_selectors = [x for x in self.ui.entry_filter_selectors.toPlainText().strip().split('\n') if x != '']
            replacements = {}
            replace_lines = [x for x in self.ui.replace_list.toPlainText().strip().split('\n') if x != '']
            for line in replace_lines:
                if "->" in line:
                    old, new = line.split("->", 1)
                    replacements[old.strip()] = new.strip()

            self.__log_message("Начинается парсинг...")

            async with (ClientSession() as session):
                if single_url != '' and single_name != '':
                    page_name = single_name + ".md"
                    await self.__process_page(session, single_url, selectors_content, save_path, page_name, header,
                                              footer, patterns, replacements, filter_selectors, save_path_2, h2, f2,
                                              single_name)
                else:
                    chapter_blocks = await self.__fetch_content(session, url, selectors_chapter_block)
                    if not chapter_blocks:
                        self.__log_message("Ошибка: Не удалось получить блоки глав")
                        raise

                    chapters = {}
                    for chapter_block in chapter_blocks:
                        chapter_name_element = chapter_block.select_one(selectors_chapter_name)

                        chapter_name = chapter_name_element.get_text(strip=True) if chapter_name_element else \
                            "Без названия"
                        chapter_name = self.__clear_filename(chapter_name)
                        chapters[chapter_name] = chapter_block.select(selectors_page)

                    tasks = []
                    for chapter, pages in chapters.items():

                        chapter_path = path.join(save_path, chapter)
                        chapter_path2 = path.join(save_path_2, chapter)
                        for id_page in range(len(pages)):
                            page_url = pages[id_page].get('href')
                            absolute_url = urljoin(url, page_url)
                            title = pages[id_page].get_text(strip=True)
                            title = self.__clear_filename(title)
                            page_name = str(id_page + 1) + ". " + title + ".md"
                            tasks.append(
                                self.__process_page(session, absolute_url, selectors_content, chapter_path, page_name,
                                                    header, footer, patterns, replacements, filter_selectors,
                                                    chapter_path2, h2, f2, title))

                    await gather(*tasks)

            self.__log_message("Парсинг завершен")
        except Exception as e:
            self.__log_message(f"Необработанная ошибка: {e}")
        finally:
            self.running = False

    def __save_config(self):
        config = {
            "url": self.ui.entry_url.text(),
            "save_path": self.ui.entry_path.text(),
            "path_2": self.ui.entry_path2.text(),
            "header": self.ui.entry_header.toPlainText().strip(),
            "footer": self.ui.entry_footer.toPlainText().strip(),
            "header2": self.ui.header2.toPlainText().strip(),
            "footer2": self.ui.footer2.toPlainText().strip(),
            "selectors_content": self.ui.content.text(),
            "selectors_chapter_block": self.ui.chapter_block.text(),
            "selectors_chapter_name": self.ui.chapter_name.text(),
            "selectors_page": self.ui.page.text(),
            "patterns": [x for x in self.ui.entry_regex.toPlainText().strip().split('\n') if x != ""],
            "filter_selectors": [x for x in self.ui.entry_filter_selectors.toPlainText().strip().split('\n') if
                                 x != ""],
            "replacements": {line.split("->")[0].strip(): line.split("->")[1].strip()
                             for line in self.ui.replace_list.toPlainText().strip().split('\n') if "->" in line}
        }
        file_path, _ = QFileDialog.getSaveFileName(
            parent=None,
            caption="Сохранить файл",
            dir="",
            filter="JSON файлы (*.json)",
            selectedFilter="*.json"
        )

        if file_path:
            if not file_path.endswith('.json'):
                file_path += '.json'
            with open(file_path, "w", encoding="utf-8") as f:
                dump(config, f, indent=4, ensure_ascii=False)
            self.__log_message(f"Конфигурация сохранена: {file_path}")

    def __load_config(self):
        file_path, _ = QFileDialog.getOpenFileName(
            parent=None,
            caption="Открыть файл",
            dir="",
            filter="JSON файлы (*.json)"
        )
        if file_path:
            self.__load_config_from(file_path)

    def __load_config_from(self, file_path: str = None):
        config = loads("""{
            "url": "https://metanit.com/web/javascript/",
            "save_path": "C:/knowledge/Temp/js",
            "path_2": "C:/knowledge/Development/1. Languages/JS",
            "header": "Составь конспект по статье:\\n```",
            "footer": "```",
            "header2": "#JS\\n# <font color=\\"#00b0f0\\">JS:</font> {%title%}",
            "footer2": "---\\n### Outer links:\\n- {%link%}",
            "selectors_chapter_block": "#container > div.outercontainer > div.innercontainer > div.item.center.menC > ol > li",
            "selectors_chapter_name": "li > p > a",
            "selectors_page": "li > ol > li > p > a",
            "selectors_content": "#container > div.outercontainer > div.innercontainer > div.item.center.menC",
            "patterns": [
                "<[^><]+>"
            ],
            "filter_selectors": [
                "div.toolbar",
                "td.gutter",
                "div.nav",
                "div.socBlock",
                "style",
                "div.date",
                "div.commentABl"
            ],
            "replacements": {
                "&lt;": "<",
                "&gt;": ">"
            }
        }""")
        if file_path is not None:
            with open(file_path, "r", encoding="utf-8") as f:
                config = load(f)

        self.ui.entry_url.setText(config.get("url", ""))
        self.ui.entry_path.setText(config.get("save_path", ""))
        self.ui.entry_path2.setText(config.get("path_2", ""))

        self.ui.entry_header.setPlainText(config.get("header", ""))
        self.ui.entry_footer.setPlainText(config.get("footer", ""))
        self.ui.header2.setPlainText(config.get("header2", ""))
        self.ui.footer2.setPlainText(config.get("footer2", ""))

        self.ui.content.setText(config.get("selectors_content", ""))
        self.ui.page.setText(config.get("selectors_page", ""))
        self.ui.chapter_block.setText(config.get("selectors_chapter_block", ""))
        self.ui.chapter_name.setText(config.get("selectors_chapter_name", ""))

        self.ui.entry_regex.setPlainText("\n".join(config.get("patterns", [])))
        self.ui.entry_filter_selectors.setPlainText("\n".join(config.get("filter_selectors", [])))
        self.ui.replace_list.setPlainText(
            "\n".join([f"{k} -> {v}" for k, v in config.get("replacements", {}).items()]))

        self.__log_message("Конфигурация загружена")

    async def __process_page(self, session: ClientSession, url, selector, chapter_path1, filename, header1, footer1,
                             patterns, replacements, filter_selectors, chapter_path2, h2, f2, title):
        content_block = await self.__fetch_content(session, url, selector)
        if content_block:
            cleaned_text = self.__clean_text(content_block, patterns, replacements, filter_selectors)
            self.__save_content(chapter_path1, chapter_path2, filename, header1, cleaned_text, footer1, h2, f2, url,
                                title)

    def __on_start(self):
        if not self.running:
            Thread(target=lambda: run(self.__parse()), daemon=True).start()
            self.running = True


if __name__ == "__main__":
    app = QApplication(argv)
    window = MainWindow()
    window.show()
    exit(app.exec())
