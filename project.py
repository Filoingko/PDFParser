import PyPDF2

import re

import nltk
from nltk.tokenize import RegexpTokenizer
from nltk.tokenize import regexp_tokenize

#using PyPDF2 extact data from pdf
pdfFileObj = open('5985.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
numofPages = pdfReader.numPages

print numofPages
#for i in range(1, numofPages) : #use to extract data from all pages.
pageObj = pdfReader.getPage(1)

#extract text from selected page
extract_text =  pageObj.extractText() 

#-----------------------------------------------------------------------------------------------------


haRegex = re.compile(r'\d'+'\.')

tokenizer = RegexpTokenizer(haRegex ,gaps=True) #re{ n}
#manipulate_text = regexp_tokenize(extract_text, pattern=haRegex) #'\d+|\$[\d\.]+|\S+'

manipulate_text = tokenizer.tokenize(extract_text)



for i in range(1,len(manipulate_text)):
    if(i == haRegex) :
        print "\n\n\n"
    print (manipulate_text[i])


#print (manipulate_text[2])

#print len(manipulate_text)




