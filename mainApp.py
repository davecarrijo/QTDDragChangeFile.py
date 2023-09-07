import sys
import os
import PyPDF2
from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap


class ImageLabel(QLabel):
    def __init__(self):
        super().__init__()

        self.setAlignment(Qt.AlignCenter)
        self.resize(400, 400)
        self.setText('\n\n Drop File Here \n\n')
        self.setStyleSheet('''
                      QLabel{
                        border: 4px dashed #aaa
                      }
                      ''')

    def setPixmap(self, image):
        super().setPixmap(image)


file_path = []


class AppDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(400, 400)

        self.setAcceptDrops(True)

        mainLayout = QVBoxLayout()
        self.photoViewer = ImageLabel()
        mainLayout.addWidget(self.photoViewer)
        self.setLayout(mainLayout)

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
            # Set the image in the Qlabel
            # self.set_image(file_path)
            self.resize(400, 400)
            print(file_path)
            path = file_path

                # start Pypdf2
            def PDFrotate(origFileName, newFileName, rotation):

                # creating a pdf File object of original pdf
                pdfFileObj = open(origFileName, 'rb')

                # creating a pdf Reader object
                pdfReader = PyPDF2.PdfReader(pdfFileObj)

                # creating a pdf writer object for new pdf
                pdfWriter = PyPDF2.PdfWriter()

                # rotating each page
                for page in range(len(pdfReader.pages)):

                    # creating rotated page object
                    pageObj = pdfReader.pages[page]
                    pageObj.rotate(rotation)

                    # adding rotated page object to pdf writer
                    pdfWriter.add_page(pageObj)

                    # new pdf file object
                    newFile = open(newFileName, 'wb')

                    # writing rotated pages to new file
                    pdfWriter.write(newFile)

                # closing the original pdf file object
                pdfFileObj.close()

                # closing the new pdf file object
                newFile.close()


            def main():

                # original pdf file name
                # origFileName = 'example.pdf'
                origFileName = file_path

                # new pdf file name
                newFileName = f"{origFileName} Altered.pdf"
                print(file_path)

                # rotation angle
                rotation = 180

                # calling the PDFrotate function
                PDFrotate(origFileName, newFileName, rotation)

                main()
        else:
            event.ignore()

    def set_image(self, file_path):
        self.photoViewer.setPixmap(QPixmap(file_path))

def app():
    app = QApplication(sys.argv)
    demo = AppDemo()
    demo.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    app()
