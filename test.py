import PyPDF2

import re

import unicodedata

import nltk
from nltk.tokenize import RegexpTokenizer
from nltk.tokenize import regexp_tokenize
from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize

#using PyPDF2 extact data from pdf
pdfFileObj = open('5985.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
numofPages = pdfReader.numPages

print (numofPages)
#for i in range(1, numofPages) : #use to extract data from all pages.
pageObj = pdfReader.getPage(1)

#extract text from selected page
#raw text
extract_text_raw =  pageObj.extractText() 

extract_text = unicodedata.normalize('NFKD', extract_text_raw).encode('ascii','ignore')

print (extract_text_raw.encode('utf-8'))

#-----------------------------------------------------------------------------------------------------
'''
sentev = word_tokenize(extract_text)


print sentev


#raw text break in to sentences
sentences = sent_tokenize(extract_text)

tokenizer = RegexpTokenizer(" " ,gaps=True) #re{ n}
#manipulate_text = regexp_tokenize(extract_text, pattern=haRegex) #'\d+|\$[\d\.]+|\S+'

manipulate_text = tokenizer.tokenize(extract_text)

haRegex = re.compile('\d{1}\.')

tempstore = []
store = []
t=0
k=1
same = 'name'
val1 = 0

for i in range(1,len(manipulate_text)):
    #print manipulate_text
    textword = manipulate_text[i]
    #print textword
    for j in range(0,len(textword)) :
        chunk = textword[j:j+2]
        #print chunk
        if haRegex.match(chunk) :
            print (chunk)
            t=t+1
        

        if 1<=t :
            if k==t :
               if (same != textword):
                    same = textword
                    tempstore.append(textword)
                    #print 'ok'
            else:
                senten = " ".join(tempstore)
                store.append(senten)
                del tempstore[:]
                k = t

#for n in (store) :
 #   print (n + "\n\n")

print store[0]
print (same)
print (val1)


#print (manipulate_text[2])

#print len(manipulate_text)
'''