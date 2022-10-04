In = open("test.txt","r")

Freq = {}

for Line in In:
    Line = Line.strip()
    for i in range(len(Line)):
        if Freq.get((Line[i])):
            Freq[Line[i]] += 1
        else:
            Freq[Line[i]] = 1

for key in Freq:
    print(str(key) + ' : ' + str(Freq[key]))

In.close()

