import hashlib

# initializing string
#str = "avocado"
#result = hashlib.sha256(str.encode())
#print(result.hexdigest())
"""
with open("names.txt") as f:
    li = f.readlines()

for i in range(len(li)):
    try:
        name = li[i]
        name = name[0:len(name)-1]
        names = name.split(" ")[0]
        name = names[0].upper() + name[1:]
    except IndexError:
        pass
    if(hashlib.sha256(name.encode()).hexdigest() == "f9c9baac9006160a6d84a09e77cbfeac349c861513e1786ea447e00198068e20"):
        print(name)
"""
stre = "f95xqUeceLf3hMURrkNPAERagYjXn1zKCn7dfP1E48aV0jE9JIIvwqFzgOBwEKJrB2i+WKJosU4DGR0gj9blIxi0pzKJc/CnmC4kltetXm+VTbTqS41JvTMrpt48y225bzEN0xOKnciVK1fr8UtsCqO24cFurEBZY6ZO4vxXLGouEYH9NynQpVtNTGwIErjWpXvBPYdPP0CGujUowW5XfUtmQghnCgbsWT/1w622Y392g+AU7T5SyiRaB0MJB9n1ByINW5XHgyjvw51sV2EIB4jYvXvPanHBaIyubCTc6HVQ5wvZXpWjvf9+gWf/W7RA"
passw = "matthew xu"
stroodle = ""
passtroodle = ""
for i in stre:  # turns text into binary
    stroodle += '{0:08b}'.format(ord(i))
for x in passw:  # turns text into binary
    passtroodle += '{0:08b}'.format(ord(x))
ans = ""
for x in range(len(stroodle)):
    if stroodle[x] == passtroodle[x%len(passtroodle)]:
        ans += "0"
    else:
        ans += "1"

realans = ""
for x in range(len(ans)//8): #turns binary into ascii/readable text
    realans += chr(int(ans[x*8:x*8+8], 2))
print(realans)