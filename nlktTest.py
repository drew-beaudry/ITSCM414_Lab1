import nltk

nltk.download('gutenberg')
nltk.download('punkt')

from nltk.corpus import gutenberg
from pprint import pprint

alice = gutenberg.raw(fileids='carroll-alice.txt')
print('the number of characters in alice is: ' + str(len(alice)))

default_st = nltk.sent_tokenize
alice_sent = default_st(text=alice)
print('total sentences in alice: ' + str(len(alice_sent)))

print('First five sentences in Alice:')
pprint(alice_sent[0:5])

sent = "The quick brown fox jumps over the lazy dog. 2-25-2020"
default_wt = nltk.word_tokenize
words = default_wt(sent)
print(sent)
print()
print(words)

wordpunkt_wt = nltk.WordPunctTokenizer()
words = wordpunkt_wt.tokenize(sent)
print(words)
