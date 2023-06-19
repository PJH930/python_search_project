import os
import data
import shutil
import subprocess
import sys
from datetime import time
from distutils.dir_util import copy_tree

import qdarkstyle
from PyQt5.QtCore import QProcess, pyqtSignal, QSize, QModelIndex
from PyQt5.QtGui import QStandardItemModel
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.Qt import Qt
import matplotlib.pyplot as plt
from click import command
from isapi.threaded_extension import WorkerThread

# from PyQt5.QtWidgets.QGridLayout import setGeometry

# UI파일 연결
# 단, UI파일은 Python 코드 파일과 같은 디렉토리에 위치해야한다.
form_class = uic.loadUiType("select_word_GUI.ui")[0]


class WindowClass(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        # setFixedSize : 윈도우 창 사이즈 고정하기
        self.setFixedSize(QSize(821, 519))
        self.setupUi(self)

        # 검색어 저장공간
        self.search_word_save = []

        # 검색 가능 리스트
        self.my_dict = data.my_dict
        self.search_word_all = self.my_dict

        # 검색버튼
        self.pushButton_1.clicked.connect(self.search_word)

        # 검색 가능 리스트 버튼
        self.pushButton_2.clicked.connect(self.search_word_list)

    #   ----------------------------↓↓↓함수들↓↓↓-----------------------------------

    # 검색버튼 함수
    def search_word(self):
        self.label.clear()
        word = self.lineEdit.text()
        self.search_word_save.append(word)
        for val in self.search_word_all.keys():
            if val.upper().find(word.upper()) >= 0:
                self.label.setText(f'{self.search_word_all[val]}')
        print('search word:', word)

    # 검색 가능 리스트보여주기
    def search_word_list(self):
        self.label.clear()
        search_key = self.search_word_all.keys()
        list = ""
        for key in search_key:
            list += (f'{key}\n\n')
        self.label.setText(f'{list}')

#   ----------------------------↑↑↑함수들↑↑↑-----------------------------------

    # 데이터셋이 들어있는 폴더를 선택하는 함수
    # def attachFile_2(self):
    #     file_path = QFileDialog.getExistingDirectory(self, "select Directory")
    #     self.textEdit_2.setText(file_path)
    #     self.dataset_list_dir[0] = file_path
    #     print('Selected Dir:', file_path)
    #     # 선택한 데이터셋 폴더 안의 파일들을 전부 file_list에 저장 후 textEdit에 보여줌
    #     file_list = os.listdir(file_path)
    #     self.textEdit.clear()
    #     for file in file_list:
    #         exist = self.textEdit.toPlainText()
    #         self.textEdit.setText(f'{exist} {file}\n')
    # 실행버튼 함수
    # def runFile(self):
    #     # 분석할 데이터셋폴더 파일들을 >> 덮어쓰기 >> 모델 데이터셋 폴더로
    #     copy_tree(self.dataset_list_dir[0], self.dataset_dir[0])
    #     # 모델의 실행파일을 실행
    #     file_path = self.open_list[0]
    #     process = QProcess(self)
    #     process.start('python', [file_path])
    # 데이터셋을 적용할 폴더 선택 함수
    # def datasetDir(self):
    #     directory_path = QFileDialog.getExistingDirectory(self, "select Directory")
    #     self.textEdit_4.setText(directory_path)
    #     self.dataset_dir[0] = directory_path

if __name__ == "__main__":
    # QApplication : 프로그램을 실행시켜주는 클래스
    app = QApplication(sys.argv)
    # WindowClass의 인스턴스 생성
    myWindow = WindowClass()
    # 프로그램 화면을 보여주는 코드
    myWindow.show()
    # 프로그램을 이벤트루프로 진입시키는(프로그램을 작동시키는) 코드
    app.exec_()
