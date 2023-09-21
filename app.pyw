import sys
import os
from PyQt5.QtWidgets import QLabel, QWidget, QApplication, QVBoxLayout, QPushButton
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap



class ImageLabel(QLabel):
    def __init__(self):
        super().__init__()

        self.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.resize(300, 300)
        self.setText('\n\n Drop File Here \n\n')
        self.setStyleSheet('''
                      QLabel{
                        border: 4px dashed #aaa
                      }
                      ''')

    def setPixmap(self, image):
        super().setPixmap(image)


class AppDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(400, 400)

        self.setAcceptDrops(True)

        mainLayout = QVBoxLayout()
        self.photoViewer = ImageLabel()
        mainLayout.addWidget(self.photoViewer)
        self.setLayout(mainLayout)
        self.OpenFolder()
# Open Folder button



    def dragEnterEvent(self, event):
        if event.mimeData().hasImage:
            event.accept()
        else:
            event.ignore()

    def dragMoveEvent(self, event):
        if event.mimeData().hasImage:
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event):
        if event.mimeData().hasImage:
            event.setDropAction(Qt.CopyAction)
            file_path = event.mimeData().urls()[0].toLocalFile()
            self.resize(400, 400)
            print(file_path)
            lines = f'origFile = "{file_path}" '
            with open('./Path_FilePy.py', 'w') as f:
                for line in lines:
                    f.write(line)

        else:
            event.ignore()




    def OpenFolder(self):
        self.OpenFolderBtn = QPushButton('Start', self)
        self.OpenFolderBtn.clicked.connect(self.clickMethodFolder)
        self.OpenFolderBtn.resize(100, 50)
        self.OpenFolderBtn.move(150, 220)
        self.OpenFolderBtn.setStyleSheet("background-color : none;")

    def clickMethodFolder(self):
        import PyPDFScript as PyScript
        ClickAction = PyScript
        ClickAction.mainDef()


    def set_image(self, file_path):
        self.photoViewer.setPixmap(QPixmap(file_path))


def app():
    app = QApplication(sys.argv)
    demo = AppDemo()
    demo.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    app()
