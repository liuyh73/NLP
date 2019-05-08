import nltk
import re
from nltk.corpus import stopwords
from nltk.corpus import brown
import numpy as np
def job1(text):
    # 分词
    words = nltk.word_tokenize(text)
    # 去掉停用词
    # stops = set(stopwords.words('english'))
    # words = [word for word in words if word.lower() not in stops]
    # # 去标点符号
    # new_words=[]
    # illegal_char = string.punctuation + u'.,;《》？！“”‘’@#￥%…&×（）——+【】{};；●，。&～、|\s:：'
    # pattern = re.compile('[%s]'%re.escape(illegal_char))
    # for word in words:
    #     new_word = pattern.sub(u'',word)
    #     if not new_word == u'':
    #         new_words.append(new_word)
    print(nltk.pos_tag(words))

def job2(words, depth):
	grammar = nltk.CFG.fromstring("""
		S -> NP VP
		VP -> VBD NP | VBD NP PP
		PP -> IN NP
		NP -> DT NN | DT NN PP
		DT -> "the" | "a"
		NN -> "boy" | "dog" | "rod"
		VBD -> "saw"
		IN -> "with"
		""")
	words = nltk.word_tokenize("the boy saw the dog with a rod")
	tags = nltk.pos_tag(words)
	rd_parser = nltk.RecursiveDescentParser(grammar)
	for tree in rd_parser.parse(words):
		print(tree)

if __name__ == "__main__":
    text = "the lawyer questioned the witness about the revolver"
    job1(text)
    job2(nltk.pos_tag(nltk.word_tokenize("the boy saw the dog with a rod")), 0)
