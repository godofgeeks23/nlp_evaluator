from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

from nltk.corpus import stopwords
import nltk


source = urlopen('https://en.wikipedia.org/wiki/Narendra_Modi').read()# Make a soup 

soup = BeautifulSoup(source,'lxml')

set([text.parent.name for text in soup.find_all(text=True)])
text = ''
for paragraph in soup.find_all('p'):
    text += paragraph.text    
text = re.sub(r'\[.*?\]+', '', text)
text = text.replace('\n', '')

# print(text.encode('utf-8')) 

# file1 = open("myfile.txt","w")#write mode
# file1.write(text)
# file1.close()
# --------------------------------------------
tokens = [t for t in text.split()]

sr = stopwords.words('english')
clean_tokens = tokens[:] 
for token in tokens:
    if token in stopwords.words('english'):
        clean_tokens.remove(token)

freq = nltk.FreqDist(clean_tokens)

# for key,val in freq.items():
    # print(str(key) + ':' + str(val))

freq.plot(20, cumulative=False)