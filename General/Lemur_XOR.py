from PIL import Image
from urllib.request import urlopen
from pathlib import Path

lemur = Image.open(urlopen("https://cryptohack.org/static/challenges/lemur_ed66878c338e662d3473f0d98eedbd0d.png"))
flag = Image.open(urlopen("https://cryptohack.org/static/challenges/flag_7ae18c704272532658c10b5faad06d74.png"))

lemurdata = list(lemur.getdata())
flagdata  = list(flag.getdata())
print(flag.size)
print(lemur.size)
newimgdata = []
temp = []
for x in range(len(lemurdata)):
    temp = []
    for y in range(3):
        temp.append((flagdata[x][y] + lemurdata[x][y]))
    newimgdata.append(tuple(temp))
newimg = Image.new(flag.mode, flag.size)
newimg.putdata(newimgdata)
newimg.show()
print(newimg.size)
