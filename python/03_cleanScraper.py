from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

source = urlopen('https://en.wikipedia.org/wiki/Narendra_Modi').read()# Make a soup 

soup = BeautifulSoup(source,'lxml')

set([text.parent.name for text in soup.find_all(text=True)])
text = ''
for paragraph in soup.find_all('p'):
    text += paragraph.text    
text = re.sub(r'\[.*?\]+', '', text)
text = text.replace('\n', '')

print(text)