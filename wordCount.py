import sys
import re
import string

textFname = sys.argv[1]
outputFname = sys.argv[2]
#dict data structure to hold words and number of them in text file.
d = dict()
with open(textFname, 'r')as file:
    for line in file:
        line = line.strip()
        line = line.lower()
        line = line.translate(line.maketrans("", "",string.punctuation))
        words = line.split(" ")
        for word in words:
            if len(word) >= 1:
                #here if word is found in d, it adds 1 to its count
                #else it adds the word and sets it to 1.
                if word in d:
                    d[word] = d[word]+1
                else:
                    d[word] = 1    
eraseFile = open(outputFname, 'w').close()
f = open(outputFname, "a")
for key in sorted(d.keys()):
    f.write(key+" "+str(d[key])+"\n")

f.close()
