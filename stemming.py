from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

ps = PorterStemmer()

example_words = ['hey', 'hi', 'hello', 'kill', 'killer', 'killing', 'my', 'mine', 'myself', 'ride', 'riding', 'rode']

for word in example_words:
    print(ps.stem(word))

new_text = "It is important to by very pythonly while you are pythoning with python. All pythoners have pythoned poorly at least once."

words = word_tokenize(new_text)
for word in words:
    print(ps.stem(word))
