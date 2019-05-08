def problem1(trainSet, standardSet):
	words=set()
	wordsOfNeg={}
	wordsOfPos={}
	wordsOfNegCount=0
	wordsOfPosCount=0
	for i in range(len(trainSet)):
		for word in trainSet[i].split(' '):
			words.add(word)
			if(standardSet[i]=='N'):
				if(wordsOfNeg.__contains__(word)):
					wordsOfNeg[word]+=1
				else:
					wordsOfNeg[word]=1
				wordsOfNegCount+=1
			else:
				if(wordsOfPos.__contains__(word)):
					wordsOfPos[word]+=1
				else:
					wordsOfPos[word]=1
				wordsOfPosCount+=1

	for word in words:
		if(wordsOfNeg.__contains__(word)):
			print("The likelihoods of word '%12s' in - sentence is: %2d/%2d"%(word, wordsOfNeg[word]+1, wordsOfNegCount+len(words)))
	for word in words:
		if(not wordsOfNeg.__contains__(word)):
			print("The likelihoods of word '%12s' not in - sentence is: %2d/%2d"%(word, 0+1, wordsOfNegCount+len(words)))
	print()
	for word in words:
		if(wordsOfPos.__contains__(word)):
			print("The likelihoods of word '%12s' in + sentence is: %2d/%2d"%(word, wordsOfPos[word]+1, wordsOfPosCount+len(words)))
	for word in words:
		if(not wordsOfPos.__contains__(word)):
			print("The likelihoods of word '%12s' not in + sentence is: %2d/%2d"%(word, 0+1, wordsOfPosCount+len(words)))
	print()
	return words, wordsOfNeg, wordsOfPos, wordsOfNegCount, wordsOfPosCount

def problem2(testSet, standardSet, words, wordsOfNeg, wordsOfPos, wordsOfNegCount, wordsOfPosCount):
	negCount=0
	posCount=0
	for i in standardSet:
		if(i=='N'):
			negCount+=1
		else:
			posCount+=1
	pOfNeg=negCount/len(standardSet)
	pOfPos=posCount/len(standardSet)

	pPredictOfNeg=pOfNeg
	pPrefictOfPos=pOfPos
	for sentence in testSet:
		for word in sentence.split(' '):
			# 计算为-的概率
			if(wordsOfNeg.__contains__(word)):
				pPredictOfNeg*=(wordsOfNeg[word]+1)/(wordsOfNegCount+len(words))
			elif(word in words):
				pPredictOfNeg*=1/(wordsOfNegCount+len(words))
			# 计算为+的概率
			if(wordsOfPos.__contains__(word)):
				pPrefictOfPos*=(wordsOfPos[word]+1)/(wordsOfPosCount+len(words))
			elif(word in words):
				pPrefictOfPos*=1/(wordsOfPosCount+len(words))
		print("The probablities that the sentence is positive and negative are: ", pPrefictOfPos, pPredictOfNeg)
		if(pPredictOfNeg < pPrefictOfPos):
			print("Thus, this sentence is of class positive")
		else:
			print("Thus, this sentence is of class negative")

if __name__ == '__main__':
	trainSet = [
		'just plain boring',
		'entirely predictable and lacks energy',
		'no surprises and very few laughs',
		'very powerful',
		'the most fun film of the summer'
	]
	standardSet=[
		'N',
		'N',
		'N',
		'P',
		'P'
	]
	testSet=[
		'predictable with no originality'
	]
	print("problem1: ")
	words, wordsOfNeg, wordsOfPos, wordsOfNegCount, wordsOfPosCount = problem1(trainSet, standardSet)
	print("problem2: ")
	problem2(testSet, standardSet, words, wordsOfNeg, wordsOfPos, wordsOfNegCount, wordsOfPosCount)