import sys
import os
from pypdf import PdfFileReader, PdfWriter, PdfFileWriter
from PyQt6.QtWidgets import QMainWindow, QLabel, QGridLayout, QWidget, QApplication, QVBoxLayout, QProgressBar, QPushButton, QFileDialog
from PyQt6.QtCore import QSize, Qt, QBasicTimer
from PyQt6.QtGui import QPixmap


# begin the pypdf part to update the files
def creat_pdf(filename):
    writer = PdfWriter()
    with open(filename, 'file') as file:
        writer.write(file)


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        self.setMinimumSize(QSize(250, 100))
        self.setMaximumSize(QSize(250, 100))
        self.setWindowTitle("EskoCrypt IMACX")

        # barra de progresso inicialização e botões
        self.OpenFolder()
        self.OpenFile()
# Open Folder button

    def OpenFolder(self):
        self.OpenFolderBtn = QPushButton('Open Folder', self)
        self.OpenFolderBtn.clicked.connect(self.clickMethodFolder)
        self.OpenFolderBtn.resize(100, 32)
        self.OpenFolderBtn.move(5, 5)
        self.OpenFolderBtn.setStyleSheet("background-color : none;")

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

# Open file button
    def OpenFile(self):
        self.OpenFileBtn = QPushButton("Open File", self)
        self.OpenFileBtn.clicked.connect(self.clickFileBtn)
        self.OpenFileBtn.resize(100, 32)
        self.OpenFileBtn.move(110, 5)
        self.OpenFileBtn.setStyleSheet("background-color : none")

    def clickFileBtn(self, file):
        # ? https://doc.qt.io/qtforpython-5/PySide2/QtWidgets/QFileDialog.html#PySide2.QtWidgets.PySide2.QtWidgets.QFileDialog.getOpenFileName
        file, check = QFileDialog.getOpenFileName(
            None,
            "QFileDialog.getOpenFileName()",
            "",
            self.tr(
                'Ilustrator (*.ia);;'
                'PDF (*.pdf)'))
        print('Clicked File button.')
        if check:
            print(file)


def main():
    app = QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
