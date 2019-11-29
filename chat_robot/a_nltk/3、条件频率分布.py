import nltk
from nltk.corpus import brown

"""
genre 是 brown 中的类别
word 是 genre类别下的所有单词
"""
genre_word = [(genre, word)
              for genre in brown.categories()
              for word in brown.words(categories=genre)
              ]

# 条件频率分布
cfd = nltk.ConditionalFreqDist(genre_word)

# 指定条件和样本作图
cfd.plot(conditions=["news", "adventure"],
         samples=[u"stock", u"sunbonnet", u"Elevated", u"narcotic", u"four",  u"woods", u"railing", u"Until",
                  u"aggression"])
# 指定条件和样本 做表格
tabulate = cfd.tabulate(conditions=["news", "adventure"],
                        samples=[u"stock", u"sunbonnet", u"Elevated", u"narcotic", u"four", u"woods", u"railing",
                                 u"Until", u"aggression"])

print(tabulate)
