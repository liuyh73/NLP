import nltk
import string
import re
from nltk.stem import LancasterStemmer
from nltk.stem import PorterStemmer 
from nltk.corpus import stopwords
from nltk.probability import FreqDist
from nltk.text import Text

def readWords():
    data = ""
    with open('data/text_en.txt', 'r', encoding='utf-8-sig') as f:
        data = f.read()
    words = nltk.word_tokenize(data)
    return words

def splitWordAndLancaster(words):
    stemmerlan = LancasterStemmer()
    wordsStem = [stemmerlan.stem(word) for word in words]
    return wordsStem

def handleStopWords(words):
    stops = set(stopwords.words('english'))
    words = [word for word in words if word.lower() not in stops]
    return words

def filterPunctuation(words):
    new_words=[]
    illegal_char = string.punctuation + u'.,;《》？！“”‘’@#￥%…&×（）——+【】{};；●，。&～、|\s:：'
    pattern = re.compile('[%s]'%re.escape(illegal_char))
    for word in words:
        new_word = pattern.sub(u'',word)
        if not new_word == u'':
            new_words.append(new_word)
    return new_words

def filterLowFrequency(words):
    threshold = 20
    new_words = []
    fdist = FreqDist(words)
    for word in fdist:
        if fdist[word] > threshold:
            new_words.append(word)
    return new_words 

def drawPlacement(words):
    text = Text(words)
    text.dispersion_plot(["Elizabeth", "Darcy", "Wickham", "Bingley", "Jane"])

def drawFreqMap(words):
    fdist = FreqDist(words)
    fdist.plot(20)

def main():
    words = readWords()
    wordsStem = splitWordAndLancaster(words)
    # print(wordsStem[:100])
    wordsStop = handleStopWords(words)
    # print(wordsStop[:100])
    wordsPunc = filterPunctuation(words)
    # print(wordsPunc[:100])
    wordsFreq = filterLowFrequency(words)
    # print(wordsFreq[:100])
    drawPlacement(words)
    drawFreqMap(filterPunctuation(handleStopWords(words)))

if __name__ == "__main__":
    main()
