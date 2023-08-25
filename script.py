import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QLabel, QGridLayout, QWidget
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtCore import QSize


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        self.setMinimumSize(QSize(400, 200))
        self.setMaximumSize(QSize(400, 200))
        self.setWindowTitle("EskoCrypt IMACX")

        pybutton = QPushButton('Open Folder', self)
        pybutton.clicked.connect(self.clickMethod)
        pybutton.resize(100, 32)
        pybutton.move(5, 5)
        pybutton.setStyleSheet("background-color : none;")

        secPyButton = QPushButton("Open File", self)
        secPyButton.clicked.connect(self.clickMethod)
        secPyButton.resize(100, 32)
        secPyButton.move(110, 5)
        secPyButton.setStyleSheet("background-color : none;")

        thirdPyButton = QPushButton("Drag & Drop", self)
        thirdPyButton.clicked.connect(self.clickMethod)
        thirdPyButton.resize(180, 180)
        thirdPyButton.move(215, 5)
        thirdPyButton.setStyleSheet("background-color : white;")

        forthPyButton = QPushButton("Start", self)
        forthPyButton.clicked.connect(self.clickMethod)
        forthPyButton.resize(205, 32)
        forthPyButton.move(5, 42)
        forthPyButton.setStyleSheet("background-color : none;")

    def clickMethod(self):
        print('Clicked Pyqt button.')


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    sys.exit(app.exec_())
