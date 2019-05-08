import spacy
nlp = spacy.load('en')

# Add neural coref to SpaCy's pipe
import neuralcoref
neuralcoref.add_to_pipe(nlp)

docs = [u'My sister has a dog. She loves him.', u'Some like to play football, others are fond of basketball', u'The more a man knows, the more he feels his ignorance.']
for doc in docs:
	print("****************分隔符****************")
	doc = nlp(doc)
	print(doc.text)
	print("上面的这句话是否包含共指指代：", doc._.has_coref)
	print("共指链为：", doc._.coref_clusters)

