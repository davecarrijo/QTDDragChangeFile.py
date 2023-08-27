import sys
import os
import typing
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QLabel, QGridLayout, QWidget, QApplication, QVBoxLayout
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtCore import QSize, Qt
from PyQt5.QtGui import QPixmap

# o get_img para a spash art do drag&drop
class ImageLabel(QLabel):
    def __init__(self):
        super().__init__()

        self.setAlignment(Qt.AlignCenter)
        self.setText('\n\n Drop image here \n\n')
        self.setStyleSheet('''
                           Qlabel{
                                border: 4px dashed #aaa
                           }
                          ''')

    def setPixmap(self, image):
        super().setPixmap(image)

#integração do drag & drop
class DragDrop(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(400, 400)
        self.setAcceptDrops(True)

        mainLayout = QVBoxLayout()

        self.photoViewer = ImageLabel()
        mainLayout.addWidget(self.photoViewer)

        self.setLayout(mainLayout)

        def dragEnterEvent(self, event):
            if event.mineData().hasImage:
                event.accept()
            else:
                event.ignore()

        def dragMoveEvent(self, event):
            if event.mineData().hasImage:
                event.accept()
            else:
                event.ignore()

        def dropEvent(self, event):
            if event.mineData().hasImage:
                event.setDropAction(Qt.CopyAction)
                file_path = event.mineData().urls()[0].toLocalFile()
                self.set_image(file_path)

                event.accept()
            else:
                event.ignore()

        def set_image(self, file_path):
            self.photoViewer.setPixmap(QPixmap(file_path))

# Janela principal
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
        pybutton.setStyleSheet("background-color : none")

        secPyButton = QPushButton("Open File", self)
        secPyButton.clicked.connect(self.clickMethod)
        secPyButton.resize(100, 32)
        secPyButton.move(110, 5)
        secPyButton.setStyleSheet("background-color : none")

        # thirdPyButton = DragDrop()
        # thirdPyButton.resize(180, 180)
        # thirdPyButton.move(215, 5)

        thirdPyButton = QPushButton("Drag & Drop", self)
        thirdPyButton.clicked.connect(self.clickMethod)
        thirdPyButton.resize(180, 180)
        thirdPyButton.move(215, 5)
        thirdPyButton.setStyleSheet("background-color : white")

        forthPyButton = QPushButton("Start", self)
        forthPyButton.clicked.connect(self.clickMethod)
        forthPyButton.resize(205, 32)
        forthPyButton.move(5, 42)
        forthPyButton.setStyleSheet("background-color : none")

    def clickMethod(self):
        print('Clicked Pyqt button.')


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

# chama a janela do progrma
    mainWin = MainWindow()
    mainWin.show()

    sys.exit(app.exec())
