from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import os
import time
import shutil
import pandas as pd
import json
import time

class Example(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setAcceptDrops(True)
        self.val = 0
        self.words = pd.read_excel(r'group.xlsx')
        self.initUI()

    def initUI(self):
        pageLayout = QHBoxLayout()
        button_layout = QVBoxLayout()
        self.stacklayout = QStackedLayout()
        self.setGeometry(600, 600, 600, 800)
        pageLayout.addLayout(self.stacklayout)

        self.setWindowTitle('Start Menu')

        button = QPushButton('Просмотреть колоды', self)
        button.clicked.connect(self.change_to_cards)
        button_layout.addWidget(button)

        button1 = QPushButton('Создать новую', self)
        button1.clicked.connect(self.change_to_creator)
        button_layout.addWidget(button1)

        button2 = QPushButton('Настройки', self)
        button2.clicked.connect(self.settings)
        button_layout.addWidget(button2)

        pageLayout.addLayout(button_layout)

        self.widget = QWidget()
        self.widget.setLayout(pageLayout)
        self.setCentralWidget(self.widget)

        self.showMaximized()

    def change_color(self):
        self.button2.setStyleSheet("QPushButton"
                             "{"
                             "background-color : green;"
                             "}"
                             )

    def change_color_2(self):
        self.button2.setStyleSheet("QPushButton"
                             "{"
                             "background-color : red;"
                             "}"
                             )

    def change_to_creator(self):
        pass

    def settings(self):
        pass

    def change_to_cards(self):
        pageLayout = QHBoxLayout()
        button_layout = QVBoxLayout()
        self.done = set()
        self.stacklayout = QStackedLayout()
        self.setGeometry(600, 600, 600, 800)

        wf = os.listdir(r'C:\Users\Миша\PycharmProjects\pythonProject4\processed')[0][:-5]
        while len(os.listdir(os.path.join(r'C:\Users\Миша\PycharmProjects\pythonProject4\crops', wf))) == 0:
            self.deal_with_empty(wf)
            if len(os.listdir(r'C:\Users\Миша\PycharmProjects\pythonProject4\crops')) > 0:
                wf = os.listdir(r'C:\Users\Миша\PycharmProjects\pythonProject4\crops')[0]

        self.graphicsView = Crops(self, working_file=wf)
        self.stacklayout.addWidget(self.graphicsView)
        pageLayout.addLayout(self.stacklayout)

        self.setWindowTitle('Test')

        self.lcd2 = QLCDNumber(self)
        self.lcd2.display(0)
        button_layout.addWidget(self.lcd2)

        button2 = QPushButton('Вперёд', self)
        button2.clicked.connect(self.next_crop)
        button_layout.addWidget(button2)
        pageLayout.addLayout(button_layout)

        button3 = QPushButton('Назад', self)
        button3.clicked.connect(self.prev_crop)
        button_layout.addWidget(button3)
        pageLayout.addLayout(button_layout)

        button4 = QPushButton('Сохранить', self)
        button4.clicked.connect(self.save_firms)
        button4.clicked.connect(self.next_crop)
        button_layout.addWidget(button4)
        pageLayout.addLayout(button_layout)

        button1 = QPushButton('Закончить', self)
        button1.clicked.connect(self.next_file_crops)
        button_layout.addWidget(button1)
        pageLayout.addLayout(button_layout)

        button = QPushButton('К файлам', self)
        button.clicked.connect(self.initUI)
        button.clicked.connect(self.play)
        button_layout.addWidget(button)

        button5 = QPushButton('Сформировать файл с базой', self)
        button5.clicked.connect(self.form_file)
        button_layout.addWidget(button5)

        self.bar = QProgressBar()
        self.bar.setMaximumWidth(250)
        button_layout.addWidget(self.bar)

        self.lcd = QLCDNumber(self)
        self.lcd.display(1)
        button_layout.addWidget(self.lcd)

        self.lcd1 = QLCDNumber(self)
        self.lcd1.display(self.graphicsView.num_crops)
        button_layout.addWidget(self.lcd1)

        self.widget = QWidget()
        self.widget.setLayout(pageLayout)
        self.setCentralWidget(self.widget)

        self.showMaximized()

    def closeEvent(self, event):
        close = QMessageBox()
        close.setText("You sure?")
        close.setStandardButtons(QMessageBox.Yes | QMessageBox.Cancel)
        close = close.exec()

        if close == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


app = QApplication(sys.argv)
window = Example()
app.exec()
sys.exit()