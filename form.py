# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'metanit-parser.ui'
##
## Created by: Qt User Interface Compiler version 6.9.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QGroupBox,
    QHBoxLayout, QLabel, QLayout, QLineEdit,
    QMainWindow, QPlainTextEdit, QPushButton, QSizePolicy,
    QSpacerItem, QTabWidget, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(934, 633)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.verticalLayout_5 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.q_tab1 = QWidget()
        self.q_tab1.setObjectName(u"q_tab1")
        self.horizontalLayout_4 = QHBoxLayout(self.q_tab1)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.verticalLayout_19 = QVBoxLayout()
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.tabWidget_2 = QTabWidget(self.q_tab1)
        self.tabWidget_2.setObjectName(u"tabWidget_2")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.verticalLayout_20 = QVBoxLayout(self.tab_3)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalLayout_14 = QVBoxLayout()
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.label = QLabel(self.tab_3)
        self.label.setObjectName(u"label")

        self.verticalLayout_14.addWidget(self.label)

        self.entry_url = QLineEdit(self.tab_3)
        self.entry_url.setObjectName(u"entry_url")

        self.verticalLayout_14.addWidget(self.entry_url)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_14.addItem(self.verticalSpacer_3)


        self.verticalLayout_20.addLayout(self.verticalLayout_14)

        self.tabWidget_2.addTab(self.tab_3, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.verticalLayout_21 = QVBoxLayout(self.tab_4)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalLayout_12 = QVBoxLayout()
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.label_5 = QLabel(self.tab_4)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout_12.addWidget(self.label_5)

        self.entry_url2 = QLineEdit(self.tab_4)
        self.entry_url2.setObjectName(u"entry_url2")

        self.verticalLayout_12.addWidget(self.entry_url2)


        self.verticalLayout_21.addLayout(self.verticalLayout_12)

        self.verticalLayout_13 = QVBoxLayout()
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.label_4 = QLabel(self.tab_4)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout_13.addWidget(self.label_4)

        self.single_file_name = QLineEdit(self.tab_4)
        self.single_file_name.setObjectName(u"single_file_name")

        self.verticalLayout_13.addWidget(self.single_file_name)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_13.addItem(self.verticalSpacer_2)


        self.verticalLayout_21.addLayout(self.verticalLayout_13)

        self.tabWidget_2.addTab(self.tab_4, "")

        self.verticalLayout_19.addWidget(self.tabWidget_2)

        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.label_2 = QLabel(self.q_tab1)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_10.addWidget(self.label_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.entry_path = QLineEdit(self.q_tab1)
        self.entry_path.setObjectName(u"entry_path")

        self.horizontalLayout_3.addWidget(self.entry_path)

        self.pushButton_5 = QPushButton(self.q_tab1)
        self.pushButton_5.setObjectName(u"pushButton_5")

        self.horizontalLayout_3.addWidget(self.pushButton_5)


        self.verticalLayout_10.addLayout(self.horizontalLayout_3)


        self.verticalLayout_19.addLayout(self.verticalLayout_10)

        self.verticalLayout_11 = QVBoxLayout()
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.label_3 = QLabel(self.q_tab1)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_11.addWidget(self.label_3)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.entry_path2 = QLineEdit(self.q_tab1)
        self.entry_path2.setObjectName(u"entry_path2")

        self.horizontalLayout_2.addWidget(self.entry_path2)

        self.pushButton_4 = QPushButton(self.q_tab1)
        self.pushButton_4.setObjectName(u"pushButton_4")

        self.horizontalLayout_2.addWidget(self.pushButton_4)


        self.verticalLayout_11.addLayout(self.horizontalLayout_2)


        self.verticalLayout_19.addLayout(self.verticalLayout_11)


        self.horizontalLayout_4.addLayout(self.verticalLayout_19)

        self.verticalLayout_18 = QVBoxLayout()
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_7 = QLabel(self.q_tab1)
        self.label_7.setObjectName(u"label_7")

        self.verticalLayout_6.addWidget(self.label_7)

        self.chapter_block = QLineEdit(self.q_tab1)
        self.chapter_block.setObjectName(u"chapter_block")

        self.verticalLayout_6.addWidget(self.chapter_block)


        self.verticalLayout_18.addLayout(self.verticalLayout_6)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_6 = QLabel(self.q_tab1)
        self.label_6.setObjectName(u"label_6")

        self.verticalLayout_7.addWidget(self.label_6)

        self.chapter_name = QLineEdit(self.q_tab1)
        self.chapter_name.setObjectName(u"chapter_name")

        self.verticalLayout_7.addWidget(self.chapter_name)


        self.verticalLayout_18.addLayout(self.verticalLayout_7)

        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_9 = QLabel(self.q_tab1)
        self.label_9.setObjectName(u"label_9")

        self.verticalLayout_8.addWidget(self.label_9)

        self.page = QLineEdit(self.q_tab1)
        self.page.setObjectName(u"page")

        self.verticalLayout_8.addWidget(self.page)


        self.verticalLayout_18.addLayout(self.verticalLayout_8)

        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.label_8 = QLabel(self.q_tab1)
        self.label_8.setObjectName(u"label_8")

        self.verticalLayout_9.addWidget(self.label_8)

        self.content = QLineEdit(self.q_tab1)
        self.content.setObjectName(u"content")

        self.verticalLayout_9.addWidget(self.content)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_9.addItem(self.verticalSpacer)


        self.verticalLayout_18.addLayout(self.verticalLayout_9)


        self.horizontalLayout_4.addLayout(self.verticalLayout_18)

        self.tabWidget.addTab(self.q_tab1, "")
        self.q_tab2 = QWidget()
        self.q_tab2.setObjectName(u"q_tab2")
        self.verticalLayout_22 = QVBoxLayout(self.q_tab2)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.frame = QFrame(self.q_tab2)
        self.frame.setObjectName(u"frame")
        self.gridLayout = QGridLayout(self.frame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_13 = QLabel(self.frame)
        self.label_13.setObjectName(u"label_13")

        self.verticalLayout_2.addWidget(self.label_13)

        self.header2 = QPlainTextEdit(self.frame)
        self.header2.setObjectName(u"header2")

        self.verticalLayout_2.addWidget(self.header2)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_10 = QLabel(self.frame)
        self.label_10.setObjectName(u"label_10")

        self.verticalLayout_3.addWidget(self.label_10)

        self.footer2 = QPlainTextEdit(self.frame)
        self.footer2.setObjectName(u"footer2")

        self.verticalLayout_3.addWidget(self.footer2)


        self.verticalLayout_2.addLayout(self.verticalLayout_3)


        self.gridLayout.addLayout(self.verticalLayout_2, 0, 3, 1, 1)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_11 = QLabel(self.frame)
        self.label_11.setObjectName(u"label_11")

        self.verticalLayout.addWidget(self.label_11)

        self.entry_header = QPlainTextEdit(self.frame)
        self.entry_header.setObjectName(u"entry_header")

        self.verticalLayout.addWidget(self.entry_header)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_12 = QLabel(self.frame)
        self.label_12.setObjectName(u"label_12")

        self.verticalLayout_4.addWidget(self.label_12)

        self.entry_footer = QPlainTextEdit(self.frame)
        self.entry_footer.setObjectName(u"entry_footer")

        self.verticalLayout_4.addWidget(self.entry_footer)


        self.verticalLayout.addLayout(self.verticalLayout_4)


        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.gridLayout.setRowStretch(0, 1)

        self.verticalLayout_22.addWidget(self.frame)

        self.label_17 = QLabel(self.q_tab2)
        self.label_17.setObjectName(u"label_17")

        self.verticalLayout_22.addWidget(self.label_17)

        self.tabWidget.addTab(self.q_tab2, "")
        self.q_tab3 = QWidget()
        self.q_tab3.setObjectName(u"q_tab3")
        self.verticalLayout_23 = QVBoxLayout(self.q_tab3)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.verticalLayout_15 = QVBoxLayout()
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.label_14 = QLabel(self.q_tab3)
        self.label_14.setObjectName(u"label_14")

        self.verticalLayout_15.addWidget(self.label_14)

        self.entry_regex = QPlainTextEdit(self.q_tab3)
        self.entry_regex.setObjectName(u"entry_regex")

        self.verticalLayout_15.addWidget(self.entry_regex)


        self.verticalLayout_23.addLayout(self.verticalLayout_15)

        self.verticalLayout_16 = QVBoxLayout()
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.label_15 = QLabel(self.q_tab3)
        self.label_15.setObjectName(u"label_15")

        self.verticalLayout_16.addWidget(self.label_15)

        self.replace_list = QPlainTextEdit(self.q_tab3)
        self.replace_list.setObjectName(u"replace_list")

        self.verticalLayout_16.addWidget(self.replace_list)


        self.verticalLayout_23.addLayout(self.verticalLayout_16)

        self.verticalLayout_17 = QVBoxLayout()
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.label_16 = QLabel(self.q_tab3)
        self.label_16.setObjectName(u"label_16")

        self.verticalLayout_17.addWidget(self.label_16)

        self.entry_filter_selectors = QPlainTextEdit(self.q_tab3)
        self.entry_filter_selectors.setObjectName(u"entry_filter_selectors")

        self.verticalLayout_17.addWidget(self.entry_filter_selectors)


        self.verticalLayout_23.addLayout(self.verticalLayout_17)

        self.tabWidget.addTab(self.q_tab3, "")

        self.verticalLayout_5.addWidget(self.tabWidget)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.q_load = QPushButton(self.centralwidget)
        self.q_load.setObjectName(u"q_load")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.q_load.sizePolicy().hasHeightForWidth())
        self.q_load.setSizePolicy(sizePolicy1)

        self.horizontalLayout.addWidget(self.q_load)

        self.q_start = QPushButton(self.centralwidget)
        self.q_start.setObjectName(u"q_start")
        sizePolicy1.setHeightForWidth(self.q_start.sizePolicy().hasHeightForWidth())
        self.q_start.setSizePolicy(sizePolicy1)

        self.horizontalLayout.addWidget(self.q_start)

        self.q_save = QPushButton(self.centralwidget)
        self.q_save.setObjectName(u"q_save")
        sizePolicy1.setHeightForWidth(self.q_save.sizePolicy().hasHeightForWidth())
        self.q_save.setSizePolicy(sizePolicy1)

        self.horizontalLayout.addWidget(self.q_save)


        self.verticalLayout_5.addLayout(self.horizontalLayout)

        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout_24 = QVBoxLayout(self.groupBox)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.log_window = QPlainTextEdit(self.groupBox)
        self.log_window.setObjectName(u"log_window")
        self.log_window.setReadOnly(True)

        self.verticalLayout_24.addWidget(self.log_window)


        self.verticalLayout_5.addWidget(self.groupBox)

        self.verticalLayout_5.setStretch(0, 8)
        self.verticalLayout_5.setStretch(1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)
        self.tabWidget_2.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Metanit Parser", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u0410\u0434\u0440\u0435\u0441 \u0441\u0442\u0440\u0430\u043d\u0438\u0446\u044b \u043e\u0433\u043b\u0430\u0432\u043b\u0435\u043d\u0438\u044f \u0440\u0430\u0437\u0434\u0435\u043b\u0430", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"\u0420\u0435\u0436\u0438\u043c \u0440\u0430\u0437\u0434\u0435\u043b\u0430", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u0410\u0434\u0440\u0435\u0441 \u0441\u0442\u0430\u0442\u044c\u0438", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u0441\u0442\u0430\u0442\u044c\u0438", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_4), QCoreApplication.translate("MainWindow", u"\u0420\u0435\u0436\u0438\u043c \u0441\u0442\u0430\u0442\u044c\u0438", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u041a\u0430\u0442\u0430\u043b\u043e\u0433 \u0441\u043e\u0445\u0440\u0430\u043d\u0435\u043d\u0438\u044f \u0442\u0435\u043a\u0441\u0442-\u0444\u0430\u0439\u043b\u043e\u0432", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u0440\u0430\u0442\u044c", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u041a\u0430\u0442\u0430\u043b\u043e\u0433 \u0441\u043e\u0445\u0440\u0430\u043d\u0435\u043d\u0438\u044f \u0444\u0430\u0439\u043b\u043e\u0432-\u0437\u0430\u0433\u043b\u0443\u0448\u0435\u043a", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u0440\u0430\u0442\u044c", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"CSS \u0441\u0435\u043b\u0435\u043a\u0442\u043e\u0440 \u043f\u0443\u043d\u043a\u0442\u0430 \u043e\u0433\u043b\u0430\u0432\u043b\u0435\u043d\u0438\u044f", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u043d\u043e\u0441\u0438\u0442\u0435\u043b\u044c\u043d\u044b\u0439 CSS \u0441\u0435\u043b\u0435\u043a\u0442\u043e\u0440 \u043d\u0430\u0437\u0432\u0430\u043d\u0438\u044f \u0433\u043b\u0430\u0432\u044b (\u043e\u0442\u043d\u043e\u0441\u0438\u0442\u0435\u043b\u044c\u043d\u043e \u0441\u0435\u043b\u0435\u043a\u0442\u043e\u0440\u0430 \u043f\u0443\u043d\u043a\u0442\u0430 \u043e\u0433\u043b\u0430\u0432\u043b\u0435\u043d\u0438\u044f)", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u043d\u043e\u0441\u0438\u0442\u0435\u043b\u044c\u043d\u044b\u0439 CSS \u0441\u0435\u043b\u0435\u043a\u0442\u043e\u0440 \u0441\u0441\u044b\u043b\u043a\u0438 \u043d\u0430 \u0433\u043b\u0430\u0432\u0443", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"CSS \u0441\u0435\u043b\u0435\u043a\u0442\u043e\u0440 \u0431\u043b\u043e\u043a\u0430 \u0441 \u0442\u0435\u043a\u0441\u0442\u043e\u043c \u043d\u0430 \u0441\u0442\u0440\u0430\u043d\u0438\u0446\u0435 \u0433\u043b\u0430\u0432\u044b", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.q_tab1), QCoreApplication.translate("MainWindow", u"\u041f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u044b \u043f\u0430\u0440\u0441\u0438\u043d\u0433\u0430", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"\u0428\u0430\u043f\u043a\u0430 \u0444\u0430\u0439\u043b\u0430-\u0437\u0430\u0433\u043b\u0443\u0448\u043a\u0438", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"\u0424\u0443\u0442\u0435\u0440 \u0444\u0430\u0439\u043b\u0430-\u0437\u0430\u0433\u043b\u0443\u0448\u043a\u0438", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"\u0428\u0430\u043f\u043a\u0430 \u0442\u0435\u043a\u0441\u0442-\u0444\u0430\u0439\u043b\u0430", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"\u0424\u0443\u0442\u0435\u0440 \u0442\u0435\u043a\u0441\u0442-\u0444\u0430\u0439\u043b\u0430", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u0438\u043c\u0435\u0447\u0430\u043d\u0438\u0435: {%link%} - \u0441\u0441\u044b\u043b\u043a\u0430 \u043d\u0430 \u0441\u0442\u0430\u0442\u044c\u044e; {%title%} - \u0437\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.q_tab2), QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0430 \u0448\u0430\u0431\u043b\u043e\u043d\u043e\u0432", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"\u0424\u0438\u043b\u044c\u0442\u0440\u0430\u0446\u0438\u044f (\u0440\u0435\u0433\u0443\u043b\u044f\u0440\u043d\u044b\u0435 \u0432\u044b\u0440\u0430\u0436\u0435\u043d\u0438\u044f, 1 \u0432\u044b\u0440./\u0441\u0442\u0440.)", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u043c\u0435\u043d\u0430 \u0432\u0445\u043e\u0436\u0434\u0435\u043d\u0438\u0439 (\u0444\u043e\u0440\u043c\u0430\u0442 \u0437\u0430\u043f\u0438\u0441\u0438: \"<find> -> <replace>\", 1 \u0437\u0430\u043c./\u0441\u0442\u0440.)", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"\u0424\u0438\u043b\u044c\u0442\u0440\u0443\u0435\u043c\u044b\u0435 CSS-\u0441\u0435\u043b\u0435\u043a\u0442\u043e\u0440\u044b (1 \u0441\u0435\u043b./\u0441\u0442\u0440.)", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.q_tab3), QCoreApplication.translate("MainWindow", u"\u041e\u0431\u0440\u0430\u0431\u043e\u0442\u043a\u0430 \u0442\u0435\u043a\u0441\u0442\u0430", None))
        self.q_load.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0433\u0440\u0443\u0437\u0438\u0442\u044c \u043a\u043e\u043d\u0444\u0438\u0433\u0443\u0440\u0430\u0446\u0438\u044e", None))
        self.q_start.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0447\u0430\u0442\u044c", None))
        self.q_save.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c \u043a\u043e\u043d\u0444\u0438\u0433\u0443\u0440\u0430\u0446\u0438\u044e", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"\u041b\u043e\u0433", None))
    # retranslateUi

