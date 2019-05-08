from nltk.corpus import wordnet as wn
import random

def problem1(words):
	for word in words:
		print("************************%s start************************"%(word))
		synsets=wn.synsets(word)
		print("同义词集：", synsets)
		for synset in synsets:
			print("--------------分隔符--------------")
			print("同义词%s中的所有词"%(synset))
			print(wn.synset(synset._name).lemma_names())
			print("同义词%s定义"%(synset))
			print(wn.synset(synset._name).definition())
			print("同义词%s例子"%(synset))
			print(wn.synset(synset._name).examples())
		print("************************%s end************************"%(word))

def problem2(words1, words2):
	# 随机选择两个词，计算语义相似度
	for i in range(len(words1)):
		print("************************%s Similarly %s************************"%(words1[i], words2[i]))
		word1Synsets=wn.synsets(words1[i])
		word2Synsets=wn.synsets(words2[i])
		num = min(len(word1Synsets), len(word2Synsets))
		randnum = random.randint(0, num-1)
		print("%s和%s的语义相似度为："%(word1Synsets[randnum]._name, word2Synsets[randnum]._name))
		print(word1Synsets[randnum].path_similarity(word2Synsets[randnum]))

def problem3(words):
	for word in words:
		print("************************%s start************************"%(word))
		synsets=wn.synsets(word)
		for synset in synsets:
			print("同义词集%s的蕴含关系为：%s"%(synset,synset.entailments()), "，反义词为：%s"%(synset.lemmas()[0].antonyms()))

if __name__ == '__main__':
	print("Problem1: ")
	words1=['dog', 'apple', 'fly']
	problem1(words1)
	print("\nProblem2: ")
	words2_1=["good", "good", "dog"]
	words2_2=["beautiful", "bad", "cat"]
	problem2(words2_1, words2_2)
	print("\nProblem3: ")
	words3 = ["walk", "supply", "hot"]
	problem3(words3)
