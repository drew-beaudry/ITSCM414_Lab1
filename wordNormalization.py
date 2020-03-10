import re
import string
import nltk
from contractions import CONTRACTION_MAP

corpus = ["The quick brown fox wasnt' that quick he couldn't wint the race",
          "Hey that's a great deal."]


def tokenize_text(text):
    sentences = nltk.sent_tokenize(text)
    word_tokens = [nltk.word_tokenize(sentence) for sentence in sentences]
    return word_tokens


tokenList = [tokenize_text(text) for text in corpus]
print("Token List:")
print(tokenList)


# Expand contractions

def expand_contractions(sentence, contraction_mapping):
    contractions_pattern = re.compile('({})'
                                      .format('|'
                                              .join(contraction_mapping.keys())), flags=re.IGNORECASE | re.DOTALL)

    def expand_match(contraction):
        match = contraction.group(0)
        first_char = match[0]
        expanded_contraction = contraction_mapping.get(match) \
            if contraction_mapping.get(match) \
            else contraction_mapping.get(match.lower())
        expanded_contraction = first_char + expanded_contraction[1:]
        return expanded_contraction

    expandedSentence = contractions_pattern.sub(expand_match, sentence)
    return expandedSentence


expandedCorpus = [expand_contractions(sentence, CONTRACTION_MAP) for sentence in corpus]
print(expandedCorpus)

# Lowercase
print(corpus[0].lower())

# Uppercase
print(corpus[1].upper())


# Remove "stopwords"
# nltk.download('stopwords')
def remove_stopwords(tokens):
    stopword_list = nltk.corpus.stopwords.words('english')
    filtered_tokens = [token for token in tokens
                       if token not in stopword_list]
    return filtered_tokens


expandedCorpusTokens = [tokenize_text(text) for text in expandedCorpus]

filteredList3 = [[remove_stopwords(tokens)
                  for tokens in sentenceTokens]
                 for sentenceTokens in expandedCorpusTokens]

print(filteredList3)

# Remove repeating characters
sampleSentence = 'My schooooooooool is reallllllly amaaaazinggg'
sampleSentenceTokens = tokenize_text(sampleSentence)

# nltk.download('wordnet')

from nltk.corpus import wordnet


def remove_repeating_characters(tokens):
    # Find characters
    repeat_pattern = re.compile(r'(\w*)(\w)\2(\w*)')

    match_substitution = r'\1\2\3'

    def replace(old_word):
        if wordnet.synsets(old_word):
            return old_word
        new_word = repeat_pattern.sub(match_substitution, old_word)
        return replace(new_word) if new_word != old_word else new_word

    # Replace
    correct_tokens = [replace(word) for word in tokens]
    return correct_tokens


print(remove_repeating_characters(sampleSentence))
