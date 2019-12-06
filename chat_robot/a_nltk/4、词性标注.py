import nltk

porter = nltk.PorterStemmer()
stem = porter.stem("lying")
print(stem)
print("============================================================")
text = nltk.word_tokenize("And now for something completely different")
tag = nltk.pos_tag(text)
"""
CC 连接词
RB 副词
IN 介词
NN 名词
JJ 形容词
PRO 代词
"""
print(tag)
print("============================================================")
print(nltk.pos_tag(["i", "love", "you"]))
print("============================================================")
sent = "我/NN 是/IN 一个/AT 大/JJ 傻×/NN"
print([nltk.tag.str2tuple(t) for t in sent.split()])
print("============================================================")
# for word in nltk.corpus.sinica_treebank.tagged_words():
#     print(word[0], word[1])
print("============================================================")
pattern = [(r".*们$", "PRO")]
tagger = nltk.RegexpTagger(pattern)
print(tagger.tag(nltk.word_tokenize("我们 累 个 去 你们 和 他们 啊")))
print("============================================================")
default_tagger = nltk.DefaultTagger("NN")
raw = "我 累 个 去"
tokens = nltk.word_tokenize(raw)
tags = default_tagger.tag(tokens)
print(tags)
print("一元标注============================================================")
tagged_sents = [[(u"我", u"PRO"), (u"小兔", u"NN")]]
unigram_tagger = nltk.UnigramTagger(tagged_sents)
# sents = nltk.corpus.brown.sents(categories="news")
sents = [[u"我", u"你", u"小兔"]]
tagger_tag = unigram_tagger.tag(sents[0])
print(tagger_tag)

# 词性标记器的存储和加载
from _pickle import dump, load

output = open("t2.pk1", "wb")
dump(unigram_tagger, output, -1)
output.close()

input = open("t2.pk1", "rb")
tagger = load(input)
input.close()
print("")
