import nltk
import urllib.request
from bs4 import BeautifulSoup
from nltk.corpus import stopwords
import re

response = urllib.request.urlopen('https://en.wikipedia.org/wiki/SpaceX')

html = response.read()

soup = BeautifulSoup(html, 'html.parser')
text = soup.get_text(strip=True)
# set([text.parent.name for text in soup.find_all(text=True)])
text = ''
for paragraph in soup.find_all('p'):
    text += paragraph.text
text = re.sub(r'\[.*?\]+', '', text)
text = text.replace('\n', '')
print(text)

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
