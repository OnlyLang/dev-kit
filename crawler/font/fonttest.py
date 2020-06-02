from fontTools.ttLib import TTFont
from fontTools import subset

font = TTFont("C:/Users/jiunl/Desktop/下载.ttf")

cmap = font.getBestCmap()
print(cmap)
print()
