from nltk.corpus import PlaintextCorpusReader

corpus_root = "D:\develop\data\my_nltk"

word_lists = PlaintextCorpusReader(corpus_root, ".*")
print(word_lists.fileids())
print(word_lists.sents("a.txt"))
print(word_lists.words("a.txt"))
