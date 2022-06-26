import wikipedia
import re
wiki = wikipedia.page('SpaceX')
text = wiki.content

text = re.sub(r'==.*?==+', '', text)
text = text.replace('\n', '')
print(text)
