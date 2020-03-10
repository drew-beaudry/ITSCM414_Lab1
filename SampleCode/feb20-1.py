# -*- coding: utf-8 -*-
"""
Created on Thu Feb 20 14:48:28 2020

@author: platta
"""

import re
"""
pattern = '.*cheese'
s1 = 'Grilled cheese is so yummy!'
s2 = 'Esther loves mac & cheese.'
s3 = 'cheese is a wisconsin passion.'
s4 = 'Cheesehead is another term for a Packers fan'
s5 = 'cheese'

print(re.match(pattern, s1, flags=re.IGNORECASE))
print(re.match(pattern, s2, flags=re.IGNORECASE))
print(re.match(pattern, s3, flags=re.IGNORECASE))
print(re.match(pattern, s4, flags=re.IGNORECASE))
print(re.match(pattern, s5, flags=re.IGNORECASE))

s6 = '0'
s7='abc123'

pattern2 = "[0-9]"
print(re.match(pattern2, s6, flags=re.IGNORECASE))
print(re.match(pattern2, s7, flags=re.IGNORECASE))

pattern3= "[^0-9]"
print(re.match(pattern3, s6, flags=re.IGNORECASE))
print(re.match(pattern3, s7, flags=re.IGNORECASE))

emailpattern="\w*@\w*\.com"
s7="alana@classmunity.com"
s8="platta@uww.edu"
print(re.match(emailpattern, s7, flags=re.IGNORECASE))
print(re.match(emailpattern, s8, flags=re.IGNORECASE))

emailpattern2="\w*@\w.*\.[com|edu|org|ca]"
print(re.match(emailpattern2, s7, flags=re.IGNORECASE))
print(re.match(emailpattern2, s8, flags=re.IGNORECASE))"""




import nltk

#nltk.download('gutenberg')
#nltk.download('punkt')

from nltk.corpus import gutenberg
from pprint import pprint


alice = gutenberg.raw(fileids='carroll-alice.txt')
print("the number of characters in alice is: "+str(len(alice)))

default_st=nltk.sent_tokenize
alice_sent=default_st(text=alice)
print('total sentences in alice"'+str(len(alice_sent)))
print("the first 5 sentences in alice are:")
pprint(alice_sent[0:5])

SENTENCE_TOKENS_PATTERN='(?<!\w\.\w\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s'
regex_st=nltk.tokenize.RegexpTokenizer(pattern=SENTENCE_TOKENS_PATTERN, gaps=True)
msg="Now we are using our regex string to tokenize. Hopefully this works!"
print(msg)

sample_sent=regex_st.tokenize(msg)
pprint(sample_sent)

sent="The quick brown fox wasn't that quick and he couldn't win the race. 2-2-14"
default_wt=nltk.word_tokenize
words=default_wt(sent)
print("now we will print out the following sentence, but word tokenized:" +sent)
print(words)

wordpunkt_wt=nltk.WordPunctTokenizer()
words=wordpunkt_wt.tokenize(sent)
print(words)

import re
import string
#from ppprint import pprint
corpus = ["The quick brown fox wasnt' that quick he couldn't wint the race", "Hey that's a greate dea"]
def tokenize_text(text):
    sentences=nltk.sent_tokenize(text)
    word_tokens = [nltk.word_tokenize(sentence) for sentence in sentences]
    return word_tokens

token_list=[tokenize_text(text) for text in corpus]
print("~~~~~~~~~the token list is:")
print(token_list)

from contractions import CONTRACTION_MAP
def expand_contractions(sentence, contraction_mapping):
    contractions_pattern = re.compile('({})'.format('|'.join(contraction_mapping.keys())), flags=re.IGNORECASE|re.DOTALL)
    
    def expand_match(contraction):
        match=contraction.group(0)
        first_char=match[0]
        expanded_contraction = contraction_mapping.get(match)\
                                if contraction_mapping.get(match)\
                                else contraction_mapping.get(match.lower())
        expanded_contraction = first_char+expanded_contraction[1:]
        return expanded_contraction
    expanded_sentence = contractions_pattern.sub(expand_match, sentence)
    return expanded_sentence

expanded_corpus = [expand_contractions(sentence, CONTRACTION_MAP) for sentence in corpus]
print(expanded_corpus)

print(corpus[0].lower())
print(corpus[0].upper())


#remove stopwords
#nltk.download('stopwords')
def remove_stopwords(tokens):
    stopword_list=nltk.corpus.stopwords.words('english')
    filtered_tokens= [token for token in tokens if token not in stopword_list]
    return filtered_tokens

expanded_corpus_tokens = [tokenize_text(text) for text in expanded_corpus]

filtered_list_3 =[[remove_stopwords(tokens)
                    for tokens in sentence_tokens]
                    for sentence_tokens in expanded_corpus_tokens]
print(filtered_list_3)

#remove repeating characters
sample_sentence = 'My schoooool is realllllyyy amaaaazingggg'
sample_sentence_tokens = tokenize_text(sample_sentence)
#nltk.download('wordnet')
"""from nltk.corpus import wordnet

def remove_repeated_characters(tokens):
    repeat_pattern= re.compile(r'(\w*)(\w)\2(\w*)')
    match_substitution = r'\1\2\3'
    def replace(old_word):
        if wordnet.synsets(old_word):
            return old_word
        new_word = repeat_pattern.sub(match_substitution, old_word)
        return replace(new_word) if new_word != old_word else new_word

    
    correct_tokens = [replace(word[0]) for word in tokens]
    return correct_tokens

print(remove_repeated_characters(sample_sentence_tokens))"""

from nltk.corpus import wordnet

def remove_repeated_characters(tokens):
    repeat_pattern = re.compile(r'(\w*)(\w)\2(\w*)')
    match_substitution = r'\1\2\3'
    def replace(old_word):
        if wordnet.synsets(old_word):
            return old_word
        new_word = repeat_pattern.sub(match_substitution, old_word)
        return replace(new_word) if new_word != old_word else new_word
            
    correct_tokens = [replace(word) for word in tokens]
    return correct_tokens

sample_sentence = 'My schooool is realllllyyy amaaazingggg'
correct_tokens = remove_repeated_characters(nltk.word_tokenize(sample_sentence))
' '.join(correct_tokens)
print(correct_tokens)
