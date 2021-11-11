from urllib.request import urlopen
from bs4 import BeautifulSoup
source = urlopen('https://en.wikipedia.org/wiki/John_D._Hunter').read()# Make a soup 
soup = BeautifulSoup(source,'lxml')
