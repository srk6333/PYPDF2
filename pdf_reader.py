import PyPDF2
#open pdf file
pdfFileObject = open(r"your_pdf_file_path", 'rb')
#Enter word to search
key = input('Enter the word to Search :')
pdfReader = PyPDF2.PdfFileReader(pdfFileObject)
count = 0
#open output file 
file = open('out_put_file','w')
print(" No. Of Pages :", pdfReader.numPages)
for i in range(pdfReader.numPages):
    pageObject = pdfReader.getPage(i)
    text = pageObject.extractText()
    #searching for key
    if key in text or key.capitalize() in text or key.upper() in text or key.lower() in text:
        count = count + 1
        print('found',i)
        file.write(str(i+1)+'\n')

print('Count of the word', count)
file.close()
pdfFileObject.close()
