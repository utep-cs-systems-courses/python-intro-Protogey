import sys
import re
import string

textFname = sys.argv[1]
outputFname = sys.argv[2]

#file = open(textFname, "r")
d = dict()
with open(textFname, 'r') as file:
    for line in file:
        line = line.strip()
        line = line.lower()
        line = line.translate(line.maketrans("", "",string.punctuation))
        words = line.split(" ")
        for word in words:
            print(word)
            if word in d:
                d[word] = d[word]+1
            else:
                d[word] = 1

eraseFile = open(outputFname, 'w').close()
f = open(outputFname, "a")
for key in sorted(d.keys()):
    key = key.strip()
    f.write(key+" "+str(d[key])+"\n")
f.close()
file.close()
