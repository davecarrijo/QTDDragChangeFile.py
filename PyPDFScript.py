import PyPDF2
import Path_FilePy


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


def mainDef():
    # original pdf file name
    origFileName = Path_FilePy.origFile
    REALPATH = origFileName.replace(".pdf", " ")
    # new pdf file name
    newFileName = f"{REALPATH}_ALTERADO.pdf"
    # rotation angle
    rotation = 180
    # calling the PDFrotate function
    PDFrotate(origFileName, newFileName, rotation)


# calling the mainDef function
if __name__ == "__main__":
    mainDef()
