PaperCountInBook = 100
StrInPaper = 50
LatterInStr = 25
SizeLatter = 4

SizeInDisk = 1.44*1024*1024
SizeBook = SizeLatter * LatterInStr * StrInPaper * PaperCountInBook

MaxBookInDisk = SizeInDisk/SizeBook

print("Количество книг, помещающихся на дискету:", round(MaxBookInDisk))
