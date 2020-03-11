import codecs
import re
import nltk

nltk.download('punkt')
nltk.download('wordnet')
from nltk.corpus import wordnet
from contractions import CONTRACTION_MAP
from nltk.stem import LancasterStemmer

files = ["resources/bostonDynamics.txt", "resources/dannyBrown.txt", "resources/kotlin.txt"]


def read_file(file_path):
    with open(file_path, encoding='utf8') as f:
        corpus = f.read()

    f.closed
    True
    return corpus


# Tokenize sentences and words
def tokenize_text(text):
    sentences = nltk.sent_tokenize(text)
    word_tokens = [nltk.word_tokenize(sentence) for sentence in sentences]
    return word_tokens


# Expand contractions
def expand_contractions(sentence, contraction_mapping):
    contractions_pattern = re.compile('({})'.format('|'.join(contraction_mapping.keys())),
                                      flags=re.IGNORECASE | re.DOTALL)

    def expand_match(contraction):
        match = contraction.group(0)
        first_char = match[0]
        expanded_contraction = contraction_mapping.get(match) \
            if contraction_mapping.get(match) \
            else contraction_mapping.get(match.lower())
        expanded_contraction = first_char + expanded_contraction[1:]
        return expanded_contraction

    expanded_sentence = contractions_pattern.sub(expand_match, sentence)
    return expanded_sentence


# Turn all text to lower case
def lowercase_text(text):
    return text.lower()


# Correct repeating characters
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


def stem(text):
    return_text = ""
    ls = LancasterStemmer()
    words = text.split()
    for word in words:
        return_text += " " + ls.stem(word)
    return return_text


# Remove special characters
def remove_special_chars(text):
    return " ".join(e for e in text if e.isalnum())


for file in files:
    text = read_file(file)
    text = expand_contractions(text, CONTRACTION_MAP)
    text = tokenize_text(text)
    text = [lowercase_text(sentence) for something in text for sentence in something]
    text = remove_repeated_characters(text)
    text = remove_special_chars(text)
    text = stem(text)
    # Print output to console
    print("filename: " + file)
    print(text)
    print("\n")
    # Write out to file
    with codecs.open(file.replace(".txt", "_out_stemmed.txt"), "w", "utf-8-sig") as temp:
        temp.write(text)
