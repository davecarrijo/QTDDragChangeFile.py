import sys
import os
import typing
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QMainWindow, QLabel, QGridLayout, QWidget, QApplication, QVBoxLayout, QProgressBar, QPushButton, QFileDialog
from PyQt6.QtCore import QSize, Qt, QBasicTimer
from PyQt6.QtGui import QPixmap


class ImageLabel(QLabel):
    def __init__(self):
        super().__init__()

        # self.setAlignment(Qt.AlignCenter)
        self.setText('\n\n Drop image here \n\n')
        self.setStyleSheet('''
                           Qlabel{
                                border: 4px dashed #aaa;
                                background-color: white;
                           }
                          ''')

    def setPixmap(self, image):
        super().setPixmap(image)


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        self.setMinimumSize(QSize(400, 200))
        self.setMaximumSize(QSize(400, 200))
        self.setWindowTitle("EskoCrypt IMACX")

        # barra de progresso inicialização e botões
        self.ProgressBarBtn()
        self.OpenFolder()
        self.OpenFile()
        self.DragDropBtn()
        self.LogArea()

# Open Folder button
    def OpenFolder(self):
        self.OpenFolderBtn = QPushButton('Open Folder', self)
        self.OpenFolderBtn.clicked.connect(self.clickMethodFolder)
        self.OpenFolderBtn.resize(100, 32)
        self.OpenFolderBtn.move(5, 5)
        self.OpenFolderBtn.setStyleSheet("background-color : none;")

    def clickMethodFolder(self):
        # https://doc.qt.io/qtforpython-5/PySide2/QtWidgets/QFileDialog.html#PySide2.QtWidgets.PySide2.QtWidgets.QFileDialog.getOpenFileName
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
        self.OpenFileBtn.clicked.connect(self.clickMethodFile)
        self.OpenFileBtn.resize(100, 32)
        self.OpenFileBtn.move(110, 5)
        self.OpenFileBtn.setStyleSheet("background-color : none")

    def clickMethodFile(self):
        # https://doc.qt.io/qtforpython-5/PySide2/QtWidgets/QFileDialog.html#PySide2.QtWidgets.PySide2.QtWidgets.QFileDialog.getOpenFileName
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

# drag & drop elements starts
    def DragDropBtn(self):
        self.setAcceptDrops(True)
        self.dragDropBtn = QLabel("Drag & Drop", self)
        self.dragDropBtn.resize(180, 180)
        self.dragDropBtn.move(215, 5)
        self.dragDropBtn.setStyleSheet("background-color : white")
        self.dragDropBtn.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.dragDropBtn.setText('\n\n Drop image here \n\n')
        self.dragDropBtn.setStyleSheet(
            "QLabel { background-color : grey; color : white; border-radius: 10px;}"
        )

        # self.photoViewer = ImageLabel()
        # mainLayout.addWidget(self.photoViewer)

        # self.setLayout(mainLayout)

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

# Log Area
    def LogArea(self):
        self.logVerb = QLabel("logs", self)
        self.logVerb.resize(205, 70)
        self.logVerb.move(5, 95)
        self.logVerb.setStyleSheet("background-color : white")
        self.logVerb.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.logVerb.setText('\n\n logs \n\n')
        self.logVerb.setStyleSheet(
            "QLabel { background-color : grey; border-radius: 2px;}"
        )

    def ProgressBarBtn(self):
        self.pbar = QProgressBar(self)
        self.pbar.setGeometry(5, 80, 205, 10)

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
            print("it Finished")
            return

        self.step = self.step + 1
        self.pbar.setValue(self.step)

    def doAction(self):
        print("it started")

        if self.timer.isActive():
            self.timer.stop()
            self.btn.setText('Start')
        else:
            self.timer.start(100, self)
            self.btn.setText('Stop')

    def keyPressEvent(self, e):
        if e.key() == Qt.Key_F1:
            os.system('xdg-open "%s"' % self.openDirectoryDialog)

# class DragDrop(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.resize(400, 400)
#         self.setAcceptDrops(True)

#         mainLayout = QGridLayout()

#         self.photoViewer = ImageLabel()
#         mainLayout.addWidget(self.photoViewer)

#         self.setLayout(mainLayout)

#         def dragEnterEvent(self, event):
#             if event.mineData().hasImage:
#                 event.accept()
#             else:
#                 event.ignore()

#         def dragMoveEvent(self, event):
#             if event.mineData().hasImage:
#                 event.accept()
#             else:
#                 event.ignore()

#         def dropEvent(self, event):
#             if event.mineData().hasImage:
#                 event.setDropAction(Qt.CopyAction)
#                 file_path = event.mineData().urls()[0].toLocalFile()
#                 self.set_image(file_path)

#                 event.accept()
#             else:
#                 event.ignore()

#         def set_image(self, file_path):
#             self.photoViewer.setPixmap(QPixmap(file_path))


# Barra de progresso funcs

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

def main():
    app = QtWidgets.QApplication(sys.argv)

    mainWin = MainWindow()
    mainWin.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
