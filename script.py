import sys
import os
import typing
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QLabel, QGridLayout, QWidget, QApplication, QVBoxLayout, QProgressBar, QPushButton
from PyQt5.QtCore import QSize, Qt, QBasicTimer
from PyQt5.QtGui import QPixmap


class ImageLabel(QLabel):
    def __init__(self):
        super().__init__()

        self.setAlignment(Qt.AlignCenter)
        self.setText('\n\n Drop image here \n\n')
        self.setStyleSheet('''
                           Qlabel{
                                border: 4px dashed #aaa;
                                background-color: white;
                           }
                          ''')

    def setPixmap(self, image):
        super().setPixmap(image)


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


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        self.setMinimumSize(QSize(400, 200))
        self.setMaximumSize(QSize(400, 200))
        self.setWindowTitle("EskoCrypt IMACX")

        # barra de progresso inicialização
        self.initUI()
        self.OpenFolder()

        OpenFileBtn = QPushButton("Open File", self)
        OpenFileBtn.clicked.connect(self.clickMethodFile)
        OpenFileBtn.resize(100, 32)
        OpenFileBtn.move(110, 5)
        OpenFileBtn.setStyleSheet("background-color : none")

        dragDropBtn = QLabel("Drag & Drop", self)
        dragDropBtn.resize(180, 180)
        dragDropBtn.move(215, 5)
        dragDropBtn.setStyleSheet("background-color : white")
        dragDropBtn.setAlignment(Qt.AlignCenter)
        dragDropBtn.setText('\n\n Drop image here \n\n')
        dragDropBtn.setStyleSheet(
            "QLabel { background-color : grey; color : white; border-radius: 10px;}")

        logVerb = QLabel("logs", self)
        logVerb.resize(205, 70)
        logVerb.move(5, 95)
        logVerb.setStyleSheet("background-color : white")
        logVerb.setAlignment(Qt.AlignLeft)
        logVerb.setText('\n\n logs \n\n')
        logVerb.setStyleSheet(
            "QLabel { background-color : white; color : orange;}")

    def clickMethodFile(self):

        print('Clicked File button.')

    def clickMethodFolder(self):
        print('Clicked Folder button.')


# Barra de progresso funcs


    def OpenFolder(self):
        self.OpenFolderBtn = QPushButton('Open Folder', self)
        self.OpenFolderBtn.clicked.connect(self.openDirectory)
        self.setCentralWidget(self.button)
        self.OpenFolderBtn.resize(100, 32)
        self.OpenFolderBtn.move(5, 5)
        self.OpenFolderBtn.setStyleSheet("background-color : none")

    # def openDirectory(self):
    #     print("Hi i am openDirectory Function . I will open Directory selected ")
    #     self.openDirectoryDialog = ddir = QFileDialog.getExistingDirectory(
    #         self, "Get Dir Path")
    #     print(self.openDirectoryDialog)

    # def keyPressEvent(self, e):
    #     if e.key() == Qt.Key_F1:
    #         os.system('xdg-open "%s"' % self.openDirectoryDialog)

    # class OpenDir(QMainWindow):
    # def __init__(self):
    #     super(OpenDir, self).__init__()
    #     # self.openDirectory()
    #     self.button = QPushButton('Open', self)
    #     self.button.clicked.connect(self.openDirectory)
    #     self.setCentralWidget(self.button)

    # def openDirectory(self):
    #     print("Hi i am openDirectory Function . I will open Directory selected ")
    #     self.openDirectoryDialog = ddir = QFileDialog.getExistingDirectory(
    #         self, "Get Dir Path")
    #     print(self.openDirectoryDialog)

    # def keyPressEvent(self, e):
    #     if e.key() == Qt.Key_F1:
    #         os.system('xdg-open "%s"' % self.openDirectoryDialog)

    def initUI(self):

        self.pbar = QProgressBar(self)
        self.pbar.setGeometry(5, 80, 240, 10)

        self.btn = QPushButton('Start', self)
        self.btn.move(5, 42)
        self.btn.resize(205, 32)
        self.btn.clicked.connect(self.doAction)

        self.timer = QBasicTimer()
        self.step = 0

    def timerEvent(self, e):

        if self.step >= 100:

            self.timer.stop()
            self.btn.setText('Finished')
            return

        self.step = self.step + 1
        self.pbar.setValue(self.step)

    def doAction(self):

        if self.timer.isActive():
            self.timer.stop()
            self.btn.setText('Start')
        else:
            self.timer.start(100, self)
            self.btn.setText('Stop')


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

# chama a janela do progrma
    mainWin = MainWindow()
    mainWin.show()

    sys.exit(app.exec_())
