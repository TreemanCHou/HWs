import re

In = open("dict.txt", "r", encoding="gbk")

inText = In.read()
inText = inText.split('\n')

Dict = {}

for lines in inText:
    k, w = lines.split('=>')
    Dict[k] = w

In.close()

while 1:
    w = input("enter q to quit :")
    if w == 'q':
        break
    if Dict.get(w):
        T = re.sub("@","\n",Dict[w])
        print(T)
    else :
        break