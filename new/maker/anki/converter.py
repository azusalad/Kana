import re

f = open('Selected Notes.txt', 'r')
c = {}
for x in f:
    a = re.findall('[一-龠]+|[ぁ-ゔ]+|[ァ-ヴー]+', x)
    b = re.findall('[a-zA-Z0-9]+|[ａ-ｚＡ-Ｚ０-９]+', x)
    c[a[0]] = b[0]
f.close()
f = open('output.txt', 'w')
f.write(str(c))
f.close()
print('Process completed')
