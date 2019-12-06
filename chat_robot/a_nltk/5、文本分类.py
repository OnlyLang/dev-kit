import nltk
from nltk.corpus import movie_reviews

my_train_set = [
    ({"feature1": u"a"}, "1"),
    ({"feature1": u"a"}, "2"),
    ({"feature1": u"a"}, "3"),
    ({"feature1": u"a"}, "3"),
    ({"feature1": u"b"}, "2"),
    ({"feature1": u"b"}, "2"),
    ({"feature1": u"b"}, "2"),
    ({"feature1": u"b"}, "2"),
    ({"feature1": u"b"}, "2"),
    ({"feature1": u"b"}, "2")
]
classifier = nltk.NaiveBayesClassifier.train(my_train_set)
print(classifier.classify({"feature1": u"a"}))
print(classifier.classify({"feature1": u"b"}))

all_words = nltk.FreqDist(w.lower() for w in movie_reviews.words())
word_features = all_words.keys()[:2000]


def document_features(document):
    features = {}
    for word in word_features:
        features["contains(%s)" % word] = (word in document)
    return features
