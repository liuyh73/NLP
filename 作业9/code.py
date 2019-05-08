import numpy as np
import pandas as pd
import re
from nltk.corpus import stopwords
from bs4 import BeautifulSoup
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.ensemble import RandomForestClassifier


def review_to_words(raw_review):
    review_text = BeautifulSoup(raw_review, "lxml").get_text()
    letters_only = re.sub("[^a-zA-Z]", " ", review_text)
    words = letters_only.lower().split()
    stops = set(stopwords.words("english"))
    meaningful_words = [w for w in words if not w in stops]
    return(" ".join(meaningful_words))


if __name__ == "__main__":
    train = pd.read_csv("data/labeledTrainData.tsv", header=0, delimiter="\t", quoting=3)
    test = pd.read_csv("data/testData.tsv", header=0, delimiter="\t", quoting=3)
    print(train.shape, test.shape)
    print("****************** Train ********************")
    train_num_reviews = len(train["review"])
    clean_train_reviews = []
    for i in range(0, train_num_reviews):
        if((i+1) % 1000 == 0):
            print("Review %d of %d\n" % (i+1, train_num_reviews))
        clean_review = review_to_words(train["review"][i])
        clean_train_reviews.append(clean_review)
    vectorizer = CountVectorizer(analyzer="word", tokenizer=None, preprocessor=None, stop_words=None, max_features=5000)
    train_data_features = vectorizer.fit_transform(clean_train_reviews)
    train_data_features = train_data_features.toarray()
    forest = RandomForestClassifier(n_estimators=100)
    forest = forest.fit(train_data_features, train["sentiment"])

    print("****************** Test ******************")
    num_reviews = len(test["review"])
    clean_test_reviews = []

    for i in range(0, num_reviews):
        clean_review = review_to_words(test["review"][i])
        clean_test_reviews.append(clean_review)

    test_data_features = vectorizer.transform(clean_test_reviews)
    test_data_features = test_data_features.toarray()
    result = forest.predict(test_data_features)
    output = pd.DataFrame(data={"id": test["id"], "sentiment": result})
    output.to_csv("Bag_of_Words_model.csv", index=False, quoting=3)
