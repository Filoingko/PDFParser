from test3 import convert_pdf_to_txt
import re

import unicodedata

import nltk
from nltk.tokenize import RegexpTokenizer
from nltk.tokenize import regexp_tokenize
from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize

path = '5985.pdf'

extract_text = convert_pdf_to_txt(path)

content = extract_text.decode('utf-8')

content = unicodedata.normalize('NFKD', content).encode('ascii','ignore')

#-----------------------------------------------------------------------------------------------------

sentev = word_tokenize(content)


#raw text break in to sentences
sentences = sent_tokenize(content)




tokenizer1 = RegexpTokenizer("\n" ,gaps=True) #re{ n}
manipulate_text1 = tokenizer1.tokenize(content)

#manipulate_text = regexp_tokenize(extract_text, pattern=haRegex) #'\d+|\$[\d\.]+|\S+'
'''
for i in (manipulate_text1) :
    print (i)
'''

haRegex = re.compile('\d{1,2}[\.]') #\d{1,2}[\,\.]{1}\d{1,2}

manipulate_text = []
manipulate_text2 = []
tempstore = []
store = []
t=0
k=1
same = 'name'
val1 = 0

#-----------------------------------------Toknize words and store array------------------------------------
for i in range(1,len(manipulate_text1)):
    #print manipulate_text1
    
    textword = manipulate_text1[i]
    #print textword

    tokenizer = RegexpTokenizer(" " ,gaps=True) #re{ n}
    temp_text = tokenizer.tokenize(textword)
    manipulate_text2.append(temp_text)

for i in (manipulate_text2) :
    for j in (i) :
        manipulate_text.append(j)


#print (manipulate_text) 

#-----------------------------------------------------------------------------------------------------

for i in manipulate_text :
    chunk = i
    #print chunk
    
    if haRegex.match(chunk) :
        #print (chunk)
        t=t+1

    if 1<=t :
        if k==t :
            if (same != chunk):
                same = chunk
                tempstore.append(chunk)
                print chunk
        else:
            senten = " ".join(tempstore)
            store.append(senten)
            del tempstore[:]
            print t
            print k
            k = t
            print store
            print t
            print k

#for n in (store) :
 #   print (n + "\n\n")


