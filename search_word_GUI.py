import sys
from PyQt5.QtCore import QProcess, pyqtSignal, QSize, QModelIndex
from PyQt5.QtWidgets import *
from PyQt5 import uic
import data

# UI파일 연결
# 단, UI파일은 Python 코드 파일과 같은 디렉토리에 위치해야한다.
form_class = uic.loadUiType("search_word_GUI.ui")[0]

class WindowClass(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        # setFixedSize : 윈도우 창 사이즈 고정하기
        self.setFixedSize(QSize(821, 519))
        self.setupUi(self)

        # 검색어 저장공간
        self.search_word_save = []

        # 검색 가능 리스트(data.py의 딕셔너리 저장값을 불러옴)
        self.my_dict = data.my_dict
        self.search_word_all = self.my_dict

        # 검색버튼
        self.pushButton_1.clicked.connect(self.search_word)

        # 검색 가능 리스트 버튼
        self.pushButton_2.clicked.connect(self.search_word_list)

    #   ----------------------------↓↓↓함수들↓↓↓-----------------------------------

    # 검색버튼 함수
    def search_word(self):
        self.textEdit.clear()
        word = self.lineEdit.text()
        self.search_word_save.append(word)
        for val in self.search_word_all.keys():
            if val.upper().find(word.upper()) >= 0:
                self.textEdit.setText(f'{self.search_word_all[val]}')
        print('search word:', word)

    # 검색 가능 리스트보여주기
    def search_word_list(self):
        self.textEdit.clear()
        search_key = self.search_word_all.keys()
        list = ""
        for key in search_key:
            list += (f'{key}\n\n')
        self.textEdit.setText(f'{list}')

#   ----------------------------↑↑↑함수들↑↑↑-----------------------------------

if __name__ == "__main__":
    # QApplication : 프로그램을 실행시켜주는 클래스
    app = QApplication(sys.argv)
    # WindowClass의 인스턴스 생성
    myWindow = WindowClass()
    # 프로그램 화면을 보여주는 코드
    myWindow.show()
    # 프로그램을 이벤트루프로 진입시키는(프로그램을 작동시키는) 코드
    app.exec_()
