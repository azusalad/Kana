import json
a=open("terms.txt","r", encoding="utf8")
b={}
c=a.read().rstrip()
a.close()
d=c.split('\n\n')
for i in d:
    e=i.split('\n')
    b[e[0]]=e[1:]
a=open('dictionary.txt','w')
a.write(json.dumps(b))
a.close()
