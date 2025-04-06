import threading
import os
import re
import json
import asyncio
import time
from urllib.parse import urljoin

import aiohttp
import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext
from bs4 import BeautifulSoup


def log_message(message):
    log_window.insert(tk.END, message + "\n")
    log_window.yview(tk.END)


semaphore = asyncio.Semaphore(5)  # Одновременно не более 5 запросов


async def fetch_content(session, url, selector):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/91.0.4472.124 Safari/537.36'}
    try:
        async with semaphore:  # Ограничение количества одновременных запросов
            await asyncio.sleep(1)  # Пауза между запросами
            async with session.get(url, headers=headers) as response:
                if response.status != 200:
                    log_message(f"Ошибка {response.status} при обращении к {url}")
                    return None
                soup = BeautifulSoup(await response.text(), 'html.parser')
                return soup.select(selector)
    except Exception as e:
        log_message(f"Ошибка запроса: {e}")
        return None


def clean_text(html_content, patterns, replacements, selectors):
    soup = BeautifulSoup(str(html_content), 'html.parser')
    if selectors:
        for selector in selectors:
            for elem in soup.select(selector):
                elem.decompose()
    text = str(soup)
    text = text.replace('<p>', '//space//').replace('</p>', '//space//')
    for i in range(1, 7):
        text = text.replace('<h'+str(i)+'>', '//space//').replace('</h'+str(i)+'>', '//space//')
    for old, new in replacements.items():
        text = text.replace(old, new)
    for pattern in patterns:
        text = re.sub(pattern, '', text)
    if len(text) > 1:
        text = text[1:-1]
    text = ''.join([line for line in text.strip().split('\n') if line.strip()])
    return '\n'.join([line for line in text.split('//space//') if line])


def save_content(path1, path2, filename, h1, content, f1, h2, f2, url, title):

    os.makedirs(path1, exist_ok=True)
    os.makedirs(path2, exist_ok=True)
    # time.sleep(1)

    with open(os.path.join(path1, filename.replace('/', ' ').replace('\\', ' ')), 'w', encoding='utf-8') as f:
        h1 = h1.replace("{%link%}", url).replace("{%title%}", title)
        f1 = f1.replace("{%link%}", url).replace("{%title%}", title)
        f.write(h1 + '\n' + content + '\n' + f1)

    with open(os.path.join(path2, filename.replace('/', ' ').replace('\\', ' ')), 'w', encoding='utf-8') as f:
        h2 = h2.replace("{%link%}", url).replace("{%title%}", title)
        f2 = f2.replace("{%link%}", url).replace("{%title%}", title)
        f.write(h2 + '\n' + f2)

    log_message(f"Файл сохранен: {filename}")


async def parse():
    log_window.delete(1.0, tk.END)
    url = entry_url.get()
    save_path = entry_path.get()
    save_path_2 = entry_path2.get()
    header = entry_header.get("1.0", tk.END).strip()
    footer = entry_footer.get("1.0", tk.END).strip()
    h2 = header2.get("1.0", tk.END).strip()
    f2 = footer2.get("1.0", tk.END).strip()
    selectors = {k: entries[k].get() for k in entries}
    patterns = entry_regex.get("1.0", tk.END).strip().split('\n')
    filter_selectors = [x for x in entry_filter_selectors.get("1.0", tk.END).strip().split('\n') if x != '']

    replacements = {}
    replace_lines = [x for x in replace_list.get("1.0", tk.END).strip().split('\n') if x != '']
    for line in replace_lines:
        if "->" in line:
            old, new = line.split("->", 1)
            replacements[old.strip()] = new.strip()

    log_message("Начинается парсинг...")

    async with aiohttp.ClientSession() as session:
        chapter_blocks = await fetch_content(session, url, selectors['chapter_block'])
        if not chapter_blocks:
            messagebox.showerror("Ошибка", "Не удалось получить блоки глав")
            return

        chapters = {}
        for chapter_block in chapter_blocks:
            chapter_name_element = chapter_block.select_one(selectors['chapter_name'])
            chapter_name = chapter_name_element.get_text(strip=True
                ).replace('/', ' ').replace('\\', ' ') if chapter_name_element else "Без названия"
            chapters[chapter_name] = chapter_block.select(selectors['page'])

        tasks = []
        for chapter, pages in chapters.items():
            chapter_path = os.path.join(save_path, chapter)
            chapter_path2 = os.path.join(save_path_2, chapter)
            for id_page in range(len(pages)):
                page_url = pages[id_page].get('href')
                absolute_url = urljoin(url, page_url)
                title = pages[id_page].get_text(strip=True)
                page_name = str(id_page+1)+". "+title + ".md"
                tasks.append(
                    process_page(session, absolute_url, selectors['content'], chapter_path, page_name, header, footer,
                                 patterns, replacements, filter_selectors, chapter_path2, h2, f2, title))

        await asyncio.gather(*tasks)

    log_message("Парсинг завершен")
    messagebox.showinfo("Готово", "Парсинг завершен")


def save_config():
    config = {
        "url": entry_url.get(),
        "save_path": entry_path.get(),
        "path_2": entry_path2.get(),
        "header": entry_header.get("1.0", tk.END).strip(),
        "footer": entry_footer.get("1.0", tk.END).strip(),
        "header2": header2.get("1.0", tk.END).strip(),
        "footer2": footer2.get("1.0", tk.END).strip(),
        "selectors": {k: entries[k].get() for k in entries},
        "patterns": [x for x in entry_regex.get("1.0", tk.END).strip().split('\n') if x != ""],
        "filter_selectors": [x for x in entry_filter_selectors.get("1.0", tk.END).strip().split('\n') if x != ""],
        "replacements": {line.split("->")[0].strip(): line.split("->")[1].strip()
                         for line in replace_list.get("1.0", tk.END).strip().split('\n') if "->" in line}
    }
    file_path = filedialog.asksaveasfilename(defaultextension=".json", filetypes=[("JSON files", "*.json")])
    if file_path:
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(config, f, indent=4, ensure_ascii=False)
        log_message("Конфигурация сохранена")


def load_config():
    file_path = filedialog.askopenfilename(filetypes=[("JSON files", "*.json")])
    if file_path:
        with open(file_path, "r", encoding="utf-8") as f:
            config = json.load(f)
        entry_url.delete(0, tk.END)
        entry_url.insert(0, config.get("url", ""))
        entry_path.delete(0, tk.END)
        entry_path.insert(0, config.get("save_path", ""))
        entry_path2.delete(0, tk.END)
        entry_path2.insert(0, config.get("path_2", ""))
        entry_header.delete("1.0", tk.END)
        entry_header.insert("1.0", config.get("header", ""))
        entry_footer.delete("1.0", tk.END)
        entry_footer.insert("1.0", config.get("footer", ""))

        header2.delete("1.0", tk.END)
        header2.insert("1.0", config.get("header2", ""))
        footer2.delete("1.0", tk.END)
        footer2.insert("1.0", config.get("footer2", ""))

        for k in entries:
            entries[k].delete(0, tk.END)
            entries[k].insert(0, config.get("selectors", {}).get(k, ""))
        entry_regex.delete("1.0", tk.END)
        entry_regex.insert("1.0", "\n".join(config.get("patterns", [])))
        entry_filter_selectors.delete("1.0", tk.END)
        entry_filter_selectors.insert("1.0", "\n".join(config.get("filter_selectors", [])))
        replace_list.delete("1.0", tk.END)
        replace_list.insert("1.0", "\n".join([f"{k} -> {v}" for k, v in config.get("replacements", {}).items()]))
        log_message("Конфигурация загружена")


# -----------------------------


async def process_page(session, url, selector, chapter_path1, filename, header1, footer1, patterns, replacements,
                       filter_selectors, chapter_path2, h2, f2, title):
    content_block = await fetch_content(session, url, selector)
    if content_block:
        cleaned_text = clean_text(content_block, patterns, replacements, filter_selectors)
        save_content(chapter_path1, chapter_path2, filename, header1, cleaned_text, footer1, h2, f2, url, title)


def run_asyncio_task(task):
    threading.Thread(target=lambda: asyncio.run(task()), daemon=True).start()


# GUI
root = tk.Tk()
root.title("Парсер")

frame_left = tk.Frame(root)
frame_left.grid(row=0, column=0, padx=10, pady=10, sticky="n")

frame_right = tk.Frame(root)
frame_right.grid(row=0, column=1, padx=10, pady=10, sticky="n")

tk.Label(frame_left, text="Ссылка на оглавление").pack()
entry_url = tk.Entry(frame_left, width=40)
entry_url.pack()

tk.Label(frame_left, text="Путь для сохранения").pack()
entry_path = tk.Entry(frame_left, width=40)
entry_path.pack()
tk.Button(frame_left, text="Выбрать", command=lambda: entry_path.insert(0, filedialog.askdirectory())).pack()

tk.Label(frame_left, text="Путь для дополнительного файла").pack()
entry_path2 = tk.Entry(frame_left, width=40)
entry_path2.pack()
tk.Button(frame_left, text="Выбрать", command=lambda: entry_path2.insert(0, filedialog.askdirectory())).pack()

labels = {
    "chapter_block": "Селектор блока главы",
    "chapter_name": "Селектор названия главы",
    "page": "Селектор ссылки",
    "content": "Селектор контента"
}

entries = {}
for key, label in labels.items():
    tk.Label(frame_left, text=label).pack()
    entries[key] = tk.Entry(frame_left, width=40)
    entries[key].pack()

tk.Label(frame_right, text="{%link%} - ссылка, {%title%} - заголовок)").pack()

tk.Label(frame_right, text="Шапка").pack()
entry_header = tk.Text(frame_right, height=2, width=40)
entry_header.pack()

tk.Label(frame_right, text="Футер").pack()
entry_footer = tk.Text(frame_right, height=2, width=40)
entry_footer.pack()

tk.Label(frame_right, text="Шапка доп. файла").pack()
header2 = tk.Text(frame_right, height=2, width=40)
header2.pack()

tk.Label(frame_right, text="Футер доп. файла").pack()
footer2 = tk.Text(frame_right, height=2, width=40)
footer2.pack()

tk.Label(frame_right, text="Фильтрация (рег. выражения, по одному в строке)").pack()
entry_regex = tk.Text(frame_right, height=4, width=40)
entry_regex.pack()

tk.Label(frame_right, text="Список замены (найти -> заменить, по одному в строке)").pack()
replace_list = tk.Text(frame_right, height=4, width=40)
replace_list.pack()

tk.Label(frame_right, text="Селекторы фильтрации контента (по одному в строке)").pack()
entry_filter_selectors = tk.Text(frame_right, height=4, width=40)
entry_filter_selectors.pack()

tk.Button(frame_left, text="Сохранить конфиг", command=save_config).pack()
tk.Button(frame_left, text="Загрузить конфиг", command=load_config).pack()
tk.Button(frame_left, text="Запустить", command=lambda: run_asyncio_task(parse)).pack()

log_window = scrolledtext.ScrolledText(root, height=10, width=85)
log_window.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

root.mainloop()
