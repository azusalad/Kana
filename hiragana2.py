"""version 3.1

3.4: added correct streaks
3.3: various improvements including dir 
3.2: added wrong detection
3.1: started session mode

2.0: added save file

1.1: added only certain character column
1.0: creation"""
import random
import json
import sys
import time
char_list=[
#1
{'あ' : ['a'],
'い' : ['i'],
'う' : ['u'],
'え' : ['e'],
'お' : ['o']},
#2
{'か' : ['ka'],
'き' : ['ki'],
'く' : ['ku'],
'け' : ['ke'],
'こ' : ['ko'],
'が' : ['ga'],
'ぎ' : ['gi'],
'ぐ' : ['gu'],
'げ' : ['ge'],
'ご' : ['go']},
#3
{'さ' : ['sa'],
'し' : ['shi'],
'す' : ['su'],
'せ' : ['se'],
'そ' : ['so'],
'ざ' : ['za'],
'じ' : ['ji'],
'ず' : ['zu'],
'ぜ' : ['ze'],
'ぞ' : ['zo'],
'ん' : ['n']},
#4
{'た' : ['ta'],
'ち' : ['chi'],
'つ' : ['tsu'],
'っ' : ['xtsu'],
'て' : ['te'],
'と' : ['to'],
'だ' : ['da'],
'ぢ' : ['di'],
'づ' : ['du'],
'で' : ['de'],
'ど' : ['do']},
#5
{'な' : ['na'],
'に' : ['ni'],
'ぬ' : ['nu'],
'ね' : ['ne'],
'の' : ['no']},
#6
{'は' : ['ha'],
'ひ' : ['hi'],
'ふ' : ['fu'],
'へ' : ['he'],
'ほ' : ['ho'],
'ば' : ['ba'],
'び' : ['bi'],
'ぶ' : ['bu'],
'べ' : ['be'],
'ぼ' : ['bo'],
'ぱ' : ['pa'],
'ぴ' : ['pi'],
'ぷ' : ['pu'],
'ぺ' : ['pe'],
'ぽ' : ['po']},
#7
{'ま' : ['ma'],
'み' : ['mi'],
'む' : ['mu'],
'め' : ['me'],
'も' : ['mo']},
#8
{'や' : ['ya'],
'ゆ' : ['yu'],
'よ' : ['yo']},
 
#9
{'ら' : ['ra'],
'り' : ['ri'],
'る' : ['ru'],
'れ' : ['re'],
'ろ' : ['ro']},
#10
{'わ' : ['wa'],
'を' : ['wo']},
#11
{'きゃ' : ['kya'],
'きゅ' : ['kyu'],
'きょ' : ['kyo'],
'ぎゃ' : ['gya'],
'ぎゅ' : ['gyu'],
'ぎょ' : ['gyo'],
'しゃ' : ['sha','shya'],
'しゅ' : ['shu','shyu'],
'しょ' : ['sho','shyo'],
'じゃ' : ['jya'],
'じゅ' : ['jyu'],
'じょ' : ['jyo'],
'ちゃ' : ['cya','chya'],
'ちゅ' : ['cyu','chyu'],
'ちょ' : ['cyo','chyo'],
'ひゃ' : ['hya'],
'ひゅ' : ['hyu'],
'ひょ' : ['hyo'],
'びゃ' : ['bya'],
'びゅ' : ['byu'],
'びょ' : ['byo'],
'ぴゃ' : ['pya'],
'ぴゅ' : ['pyu'],
'ぴょ' : ['pyo'],
'みゃ' : ['mya'],
'みゅ' : ['myu'],
'みょ' : ['myo'],
'りゃ' : ['rya'],
'りゅ' : ['ryu'],
'りょ' : ['ryo']}
]
char_dict={
'あ' : 'a',
'い' : 'i',
'う' : 'u',
'え' : 'e',
'お' : 'o',
'か' : 'ka',
'き' : 'ki',
'く' : 'ku',
'け' : 'ke',
'こ' : 'ko',
'が' : 'ga',
'ぎ' : 'gi',
'ぐ' : 'gu',
'げ' : 'ge',
'ご' : 'go',
'さ' : 'sa',
'し' : 'shi',
'す' : 'su',
'せ' : 'se',
'そ' : 'so',
'ざ' : 'za',
'じ' : 'ji',
'ず' : 'zu',
'ぜ' : 'ze',
'ぞ' : 'zo',
'ん' : 'n',
'た' : 'ta',
'ち' : 'chi',
'つ' : 'tsu',
'て' : 'te',
'と' : 'to',
'だ' : 'da',
'ぢ' : 'di',
'づ' : 'du',
'で' : 'de',
'ど' : 'do',
'な' : 'na',
'に' : 'ni',
'ぬ' : 'nu',
'ね' : 'ne',
'の' : 'no',
'は' : 'ha',
'ひ' : 'hi',
'ふ' : 'fu',
'へ' : 'he',
'ほ' : 'ho',
'ば' : 'ba',
'び' : 'bi',
'ぶ' : 'bu',
'べ' : 'be',
'ぼ' : 'bo',
'ぱ' : 'pa',
'ぴ' : 'pi',
'ぷ' : 'pu',
'ぺ' : 'pe',
'ぽ' : 'po',
'ま' : 'ma',
'み' : 'mi',
'む' : 'mu',
'め' : 'me',
'も' : 'mo',
'や' : 'ya',
'ゆ' : 'yu',
'よ' : 'yo',
'ら' : 'ra',
'り' : 'ri',
'る' : 'ru',
'れ' : 're',
'ろ' : 'ro',
'わ' : 'wa',
'を' : 'wo'
}
word_dict={
'あい' : ['love'],
'いう' : ['to say'],
'あう' : ['to meet'],
'おい' : ['hey'],
'あおい' : ['blue'],
'うえ' : ['on top'],
'うお' : ['fish'],
'いい' : ['good'],
'いいえ' : ['no'],
'ええ' : ['yes'],
'おおい' : ['many'],
'ああいう' : ['like that'],
'かく' : ['to write'],
'きく' : ['to listen'],
'こく' : ['country'],
'かき' : ['fire'],
'かう' : ['to buy'],
'かお　' : ['face'],
'こい' : ['passion','carpfish','carp'],
'おく' : ['back'],
'えき' : ['station'],
'いく' : ['to go'],
'いき' : ['mood'],
'あき' : ['autumn','fall'],
'あく' : ['evil'],
'あかい' : ['red'],
'くい' : ['regret'],
'あけ' : ['dawn'],
'おきあい' : ['coast'],
'かぎ' : ['key'],
'かいぎ' : ['meeting'],
'えがお' : ['smile'],
'えいが' : ['movie'],
'えいご' : ['english'],
'ぐあい' : ['condition'],
'かげ' : ['shadow'],
'あかい　かあ' : ['red face'],
'いい　えいが' : ['good movie'],
'ああい　かげ' : ['blue shadow'],
'すし' : ['sushi'],
'あさ' : ['morning'],
'かさ' : ['umbrella'],
'せき' : ['cough'],
'あかしい' : ['interesting'],
'すぐ' : ['immediately'],
'さ' : ['difference'],
'いし' : ['stone'],
'さがす' : ['to search'],
'さすが' : ['as expected'],
'おさけ' : ['sake'],
'しかし' : ['however'],
'すごい' : ['amazing'],
'しあい' : ['competition'],
'しずか' : ['silent'],
'がくせい' : ['student'],
'いそがしい' : ['busy'],
'そあく' : ['crude'],
'あそい' : ['late'],
'せす' : ['to erase'],
'さそう' : ['to invite'],
'かえす' : ['to return'],
'おす' : ['to push'],
'くじ' : ['lottery'],
'おさぎ' : ['rabbit'],
'きし' : ['knight'],
'しあ' : ['salt'],
'すこし' : ['a little'],
'さいせい' : ['playback'],
'すぐ' : ['immediately'],
'いしき' : ['consciousness'],
'さがす' : ['to search'],
'あかしい' : ['strange'],
'すき' : ['like'],
'しかく' : ['square'],
'がくせい' : ['student'],
'おんがく' : ['music'],
'ぎんこう' : ['bank'],
'こうえん' : ['park'],
'がかん' : ['theatre'],
'えいがかん' : ['movie theatre'],
'せん' : ['thousand'],
'あんしん' : ['relief'],
'じしん' : ['confidence'],
'おいしい' : ['delicious'],
'おかしい' : ['strange'],
'おかしい えがお' : ['strange smile'],
'すごい　えいがかん' : ['amazing theatre'],
'すぐ　いく' : ['going now'],
'いそがしい　ぎんこう' : ['busy bank'],
'さく' : ['to bloom'],
'ぞう' :  ['elephant'],
'おかし' : ['sweets'],
'あおぞら' : ['blue sky'],
'そおぞお' : ['imagination'],
'こうこうせい' : ['high school student','highschool student'],
'きあく' : ['memory'],
'さいご' : ['last'],
'くぎ' : ['hangnail','hang nail'],
'ごご' : ['5pm'],
'ここ' : ['moss'],
'こげき' : ['comedy'],
'けいこ' : [ "girl's name"],
'かお' : ['face'],
'いかが' : ['how are you?'],
'きく' : ['chrysanthemum'],
'かぐ' : ['furniture'],
'がか' : ['painter'],
'げき' : ['play'],
'かいこ' : ['discharge'],
'けいご' : ['honorific'],
'ごかい' : ['misunderstanding'],
'かがく' : ['science']
}
session_char_list=[
#1
{'あ' : [0],
'い' : [0],
'う' : [0],
'え' : [0],
'お' : [0]},
#2
{'か' : [0],
'き' : [0],
'く' : [0],
'け' : [0],
'こ' : [0],
'が' : [0],
'ぎ' : [0],
'ぐ' : [0],
'げ' : [0],
'ご' : [0]},
#3
{'さ' : [0],
'し' : [0],
'す' : [0],
'せ' : [0],
'そ' : [0],
'ざ' : [0],
'じ' : [0],
'ず' : [0],
'ぜ' : [0],
'ぞ' : [0],
'ん' : [0]},
#4
{'た' : [0],
'ち' : [0],
'つ' : [0],
'っ' : [0],
'て' : [0],
'と' : [0],
'だ' : [0],
'ぢ' : [0],
'づ' : [0],
'で' : [0],
'ど' : [0]},
#5
{'な' : [0],
'に' : [0],
'ぬ' : [0],
'ね' : [0],
'の' : [0]},
#6
{'は' : [0],
'ひ' : [0],
'ふ' : [0],
'へ' : [0],
'ほ' : [0],
'ば' : [0],
'び' : [0],
'ぶ' : [0],
'べ' : [0],
'ぼ' : [0],
'ぱ' : [0],
'ぴ' : [0],
'ぷ' : [0],
'ぺ' : [0],
'ぽ' : [0]},
#7
{'ま' : [0],
'み' : [0],
'む' : [0],
'め' : [0],
'も' : [0]},
#8
{'や' : [0],
'ゆ' : [0],
'よ' : [0]},
 
#9
{'ら' : [0],
'り' : [0],
'る' : [0],
'れ' : [0],
'ろ' : [0]},
#1[0]
{'わ' : [0],
'を' : [0]},
#11
{'きゃ' : [0],
'きゅ' : [0],
'きょ' : [0],
'ぎゃ' : [0],
'ぎゅ' : [0],
'ぎょ' : [0],
'しゃ' : [0],
'しゅ' : [0],
'しょ' : [0],
'じゃ' : [0],
'じゅ' : [0],
'じょ' : [0],
'ちゃ' : [0],
'ちゅ' : [0],
'ちょ' : [0],
'ひゃ' : [0],
'ひゅ' : [0],
'ひょ' : [0],
'びゃ' : [0],
'びゅ' : [0],
'びょ' : [0],
'ぴゃ' : [0],
'ぴゅ' : [0],
'ぴょ' : [0],
'みゃ' : [0],
'みゅ' : [0],
'みょ' : [0],
'りゃ' : [0],
'りゅ' : [0],
'りょ' : [0]}
]
dir_dict={
'1' : ['vowels'],
'2' : ['k'],
'3' : ['s'],
'4' : ['t'],
'5' : ['n'],
'6' : ['h'],
'7' : ['m'],
'8' : ['y'],
'9' : ['r'],
'10' : ['w'],
'11' : ['y diagraphs']
}
save_buffer={}
filename=".save.json"

def save():
    global save_buffer
    global filename
    with open(filename,"w",encoding="utf8") as lmao:
        lmao.write(json.dumps(save_buffer))

def load():
    global save_buffer
    global filename
    with open(filename,"a+",encoding="utf8") as lmao:
        lmao.seek(0,2)
        if lmao.tell() == 0:
            save_buffer={"chars":{},"words":{},"chars_number":0,"words_number":0}
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

if not load():
    sys.exit()
c=int(input("Mode(1=character recognition,2=word recognition,3=Character Full List)\n>"))
if c == 1:
    while True:
        a=input("Column Number (type dir for directory)\n>")
        if a == "dir":
            print(dir_dict)
        else:
            a=int(a)
            break
    d=int(input("Just that group? 1 for yes and 2 for no\n>"))
    streak = 0             
    while True:
        if d == 1:
            group_number= int(a-1)
        else:
            group_number=random.randint(0,a-1)
        random_key=random.choice(list(char_list[group_number]))
        character_list=char_list[group_number][random_key]
        if random_key not in save_buffer["chars"].keys():
            save_buffer["chars"][random_key]={"right":0,"wrong":0,"right_guesses":{},"wrong_guesses":{},"average_time":0,"times":[]}
        l=save_buffer["chars"][random_key]
        print(random_key)
        time_start=time.time()
        b=input(">")
        time_end=time.time()
        answer_time=time_end-time_start
        l["times"].append(answer_time)
        l["average_time"]=((l["right"]+l["wrong"])*l["average_time"]+answer_time)/(l["right"]+l["wrong"]+1)
        if b in character_list:
            if b in l["right_guesses"].keys():
                l["right_guesses"][b]+=1
            else:
                l["right_guesses"][b]=1
            l["right"]+=1
            streak = streak + 1                              
            print("Correct " + str(character_list))
            if streak % 10 == 0:                                
                print("Streak: " + str(streak))                                              
        else:
            if b in l["wrong_guesses"].keys():
                l["wrong_guesses"][b]+=1
            else:
                l["wrong_guesses"][b]=1
            l["wrong"]+=1
            print("WRONG " + str(character_list) + "\nStreak: " + str(streak))
            streak = 0              
        save_buffer["chars_number"]+=1
        save()
elif c == 2:
    while True:
        random_key=random.choice(list(word_dict))
        word_list=word_dict[random_key]
        if random_key not in save_buffer["words"].keys():
            save_buffer["words"][random_key]={"right":0,"wrong":0,"right_guesses":{},"wrong_guesses":{},"average_time":0,"times":[]}
        l=save_buffer["words"][random_key]
        print(random_key)
        time_start=time.time()
        b=input(">")
        time_end=time.time()
        answer_time=time_end-time_start
        l["times"].append(answer_time)
        l["average_time"]=((l["right"]+l["wrong"])*l["average_time"]+answer_time)/(l["right"]+l["wrong"]+1)
        if b.lower() in word_list:
            if b in l["right_guesses"].keys():
                l["right_guesses"][b]+=1
            else:
                l["right_guesses"][b]=1
            l["right"]+=1
            print("Correct " + str(word_list))
        else:
            if b in l["wrong_guesses"].keys():
                l["wrong_guesses"][b]+=1
            else:
                l["wrong_guesses"][b]=1
            l["wrong"]+=1
            print("WRONG " + str(word_list))
        save_buffer["words_number"]+=1
        save()
elif c == 3:
        session_finish = False
        group_number=random.randint(0,10)
        while True:
            while True:
                random_key_check=random.choice(list(char_list[group_number]))
                if session_char_list[random_key_check] == 0:
                    random_key = random_key_check
                    break
                elif 0 in session_char_list.values() == False:
                    session_finish = True
                    break
            if session_finish == False: 
                character_list=char_list[group_number][random_key]
                if random_key not in save_buffer["chars"].keys():
                    save_buffer["chars"][random_key]={"right":0,"wrong":0,"right_guesses":{},"wrong_guesses":{},"average_time":0,"times":[]}
                l=save_buffer["chars"][random_key]
                print(random_key)
                time_start=time.time()
                b=input()
                time_end=time.time()
                answer_time=time_end-time_start
                l["times"].append(answer_time)
                l["average_time"]=((l["right"]+l["wrong"])*l["average_time"]+answer_time)/(l["right"]+l["wrong"]+1)
                if b in character_list:
                    if b in l["right_guesses"].keys():
                        l["right_guesses"][b]+=1
                    else:
                        l["right_guesses"][b]=1
                    l["right"]+=1
                    print("Good")
                    session_char_list[random_key_check] = 1
                else:
                    if b in l["wrong_guesses"].keys():
                        l["wrong_guesses"][b]+=1
                    else:
                        l["wrong_guesses"][b]=1
                    l["wrong"]+=1
                    print("Bad " + str(character_list))
                    session_char_list[random_key_check] = 2
                save_buffer["chars_number"]+=1
                save()
            else:
                break
            break
        print("Session finished.")
