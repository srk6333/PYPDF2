import PyPDF2
pdfFileObject = open(r"automatetheboringstuffwithpython_new.pdf", 'rb')
key = input('Enter the word to Search :')
pdfReader = PyPDF2.PdfFileReader(pdfFileObject)
pdfWritter = PyPDF2.PdfFileWriter()
count = 0
file = open('sam.txt','w')
print(" No. Of Pages :", pdfReader.numPages)
for i in range(pdfReader.numPages):
    pageObject = pdfReader.getPage(i)
    text = pageObject.extractText()
    if key in text or key.capitalize() in text or key.upper() in text or key.lower() in text:
        count = count + 1
        print('found',i)
        file.write(str(i+1)+'\n')
        pdfWritter.addPage(pageObject)


print('Count of the word', count)
pdfOutputFile = open('output.pdf', 'wb')
pdfWritter.write(pdfOutputFile)
pdfOutputFile.close()
file.close()
pdfFileObject.close()

