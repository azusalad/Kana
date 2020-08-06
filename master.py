"""version 3.3
3.4: added dir and h column of katakana
3.3: added 2 columns of katakana
3.2: added wrong detection
3.1: started session mode
2.0: added save file
1.1: added only certain character column
1.0: creation"""

# #$ things picky needs to check
# #^ things randomguy needs to check
import random
import json
import sys
import time
import os
#use this for the save
save_buffer={}
#name of the file in which the save data is stored
filename=".save.json"

def save():
    global save_buffer
    global filename
    with open(filename,"w",encoding="utf8") as lmao:
#^ will have to change this a bit by using the .get method
        lmao.write(json.dumps(save_buffer))
def load():
    global save_buffer
    global filename
    with open(filename,"a+",encoding="utf8") as lmao:
        lmao.seek(0,2)
        if lmao.tell() == 0:
            save_buffer={
            "chars":{},
            "words":{},
            "phrases":{},
            "chars_number":0,
            "words_number":0,
            "phrases_number":0,
            }
            lmao.write(json.dumps(save_buffer))
            return 1
        else:
            try:
                lmao.seek(0,0)
                save_buffer=json.loads(lmao.read())
            except:
                print("Error loading save file. Closing program")
                return 0
            else:
                return 2
#delete comment for line below to clear screen each time program is executed
#os.system('cls' if os.name == 'nt' else 'clear')
if not load():
    sys.exit()
file_buffer=open("char_dict.json","r",encoding="utf8")
char_dict=json.loads(file_buffer.read())
file_buffer.close()
file_buffer=open("char_display_dict.json","r",encoding="utf8")
#used to display characters in english
char_display_dict=json.loads(file_buffer.read())
file_buffer.close()
file_buffer=open("word_dict.json","r",encoding="utf8")
word_dict=json.loads(file_buffer.read())
file_buffer.close()
choices={
    "hiragana":{
        "first":char_dict["hiragana"],
        "second":save_buffer["chars"],
        "third":"chars_number",
        "lower_range":0,
        "upper_range":1
    },
    "katakana":{
        "first":char_dict["katakana"],
        "second":save_buffer["chars"],
        "third":"chars_number",
        "lower_range":0,
        "upper_range":1
    },
    "words":{
        "first":word_dict["hiragana"],
        "second":save_buffer["words"],
        "third":"words_number",
        "lower_range":0,
        "upper_range":1
    },
    "phrases":{
        "first":word_dict["phrases"],
        "second":save_buffer["phrases"],
        "third":"phrases_number",
        "lower_range":0,
        "upper_range":1
    }
}
prepareddict={}
choice={}
c=int(input("Modes:\n1. Character recognition\n2. Word recognition\n3. Phrase recognition\n>"))

if c == 1:
    a=int(input("1. Hiragana\n2. Katakana\n>"))
    choice=(choices["hiragana"],choices["katakana"])[a-1]
    e=int(input("Group Number:"))
    choice["upper_range"]=e
    d=int(input("Just that group? 1 for yes 2 for no "))
    choice["lower_range"]=(e-1,0)[d-1]
elif c == 2:
    choice=choices["words"]
elif c == 3:
    choice=choices["phrases"]
    e=int(input("Group Number:"))
    choice["upper_range"]=e
    d=int(input("Just that group? 1 for yes 2 for no "))
    choice["lower_range"]=(e-1,0)[d-1]    
for i in range(choice["lower_range"],choice["upper_range"]):
    prepareddict.update(choice["first"][i])
while True:
    random_key=random.choice(list(prepareddict))
    currentlist=prepareddict[random_key]
    if random_key not in choice["second"].keys():
        choice["second"][random_key]={"right":0,"wrong":0,"right_guesses":{},"wrong_guesses":{},"average_time":0,"times":[]}
    l=choice["second"][random_key]
    print(random_key)
    time_start=time.time()
    b=input()
    time_end=time.time()
    answer_time=time_end-time_start
    l["times"].append(answer_time)
    l["average_time"]=((l["right"]+l["wrong"])*l["average_time"]+answer_time)/(l["right"]+l["wrong"]+1)
    if b.lower() in currentlist:
        if b in l["right_guesses"].keys():
            l["right_guesses"][b]+=1
        else:
            l["right_guesses"][b]=1
        l["right"]+=1
        print("Good")
    else:
        if b in l["wrong_guesses"].keys():
            l["wrong_guesses"][b]+=1
        else:
            l["wrong_guesses"][b]=1
        l["wrong"]+=1
        print("Bad " + str(currentlist))
    save_buffer[choice["third"]]+=1
    save()
