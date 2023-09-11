import sys
import os
from pypdf import PdfFileReader, PdfWriter, PdfFileWriter
from PyQt6.QtWidgets import QMainWindow, QLabel, QGridLayout, QWidget, QApplication, QVBoxLayout, QProgressBar, QPushButton, QFileDialog
from PyQt6.QtCore import QSize, Qt, QBasicTimer
from PyQt6.QtGui import QPixmap


def clickMethodFolder(self, file):
    # ? https://doc.qt.io/qtforpython-5/PySide2/QtWidgets/QFileDialog.html#PySide2.QtWidgets.PySide2.QtWidgets.QFileDialog.getOpenFileName
    file, check = QFileDialog.getOpenFileName(
        None,
        "QFileDialog.getOpenFileName()",
        "",
        self.tr(
            'All Files (*);;'
            'Folder (*.)'))

    if check:
        print(file)
    print('Clicked Folder button.')
    
    return file


a = clickMethodFolder()

print(a)
