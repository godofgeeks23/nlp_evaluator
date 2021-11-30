from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

text = """Muad'Dib learned rapidly because his first training was in how to learn. And the first lesson of all was the basic trust that he could learn. It's shocking to find how many people do not believe they can learn, and how many more believe learning to be difficult."""
print("\ntext - ", text)

sentences = sent_tokenize(text)
print("\nsentences - ", sentences)

words = word_tokenize(text)
print("\nwords - ", words)

stop_words = set(stopwords.words("english"))
filtered_list = []
for word in words:
    if word.casefold() not in stop_words:
        filtered_list.append(word)
try:
    while True:
        filtered_list.remove('.')
        filtered_list.remove(',')
        filtered_list.remove("'s")
except ValueError:
    pass
print("\nfiltered_list - ", filtered_list)
