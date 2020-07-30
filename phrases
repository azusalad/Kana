"""version 1.3

1.4: finished all katakana, added correct streaks
1.3: added h column
1.2: added n column
1.1: various improvements, added dir, added to t column
1.0: creation, added column 1"""
import random
import json
import sys
import time
char_list=[
#1
{'おはよう（ございます）' : ['good morning'],
'こんいちは' : ['good afternoon'],
'こんばんは' : ['good evening'],
'さようなら' : ['bye','goodbye','good bye'],
'おやすみ（なさい）' : ['good night'],
'ありがとう（ございます）' : ['thank you','thanks'],
'すみません' : ['sorry','excuse me'],
'いいえ' : ['no'],
'いってきます' : ["i'll go and come back"],
'いってらっしゃい' : ['please go and come back'],
'ただいま' : ["i'm home"],
'おかえり（なさい）' : ['welcome home'],
'いただきます' : ['thank you for the meal (before)'],
'ごちそうさま（でした）' : ['thank you for the meal (after)'],
'はじめまして' : ['how are you?'],
'よろしくおねがいします' : ['nice to meet you']},
#2
{'あの' : ['um'],
'いま' : ['now'],
'えいご' : ['english'],
'ええ' : ['yes'],
'がくせい' : ['student'],
'～ご' : ['~language'],
'こうこう' : ['high school','highschool'],
'ごご' : ['pm'],
'ごぜん' : ['am'],
'～さい' : ['~years old'],
'～さん' : ['san'],
'～じ' : ["o'clock"],
'せんこう' : ['major'],
'せんせい' : ['teacher'],
'そうです' : ["that's right"],
'そうですか' : ['is that so?'],
'だいがく' : ['college','university'],
'でんわ' : ['telephone'],
'ともだち' : ['friend'],
'なまえ' : ['name'],
'なに' : ['what'],
'にほん' : ['japan'],
'～ねんせい' : ['~year student'],
'はい' : ['yes'],
'はん' : ['half'],
'ばんごう' : ['number'],
'りゅうがくせい' : ['international student'],
'わたし' : ['i','me'],
'アメリカ' : ['america'],
'イギリス' : ['britain'],
'オーストラリア' : ['australia'],
'かんこく' : ['korea'],
'スウィーデン' : ['sweden'],
'ちゅうごく' : ['china'],
'かがく' : ['science'],
'けいざい' : ['economics'],
'コンピューター' : ['computer'],
'せいじ' : ['politics'],
'ビジネス' : ['business'],
'ぶんがく' : ['literature'],
'れきし' : ['history'],
'しごと' : ['job','work','occupation'],
'いしゃ' : ['doctor'],
'かいしゃいん' : ['office worker'],
'こうこうせい' : ['highschool student','high school student'],
'しゅふ' : ['housewife'],
'だいがくいんせい' : ['graduate student'],
'だいがくせい' : ['college student'],
'べんごし' : ['lawyer'],
'おかあさん' : ['mother'],
'おとうさん' : ['father'],
'おねえさん' : ['older sister'],
'おにいさん' : ['older brother'],
'いもうと' : ['younger sister'],
'おとうと' : ['younger brother']},
#3
{'サ' : ['sa'],
'シ' : ['shi'],
'シェ' : ['she'],
'ス' : ['su'],
'セ' : ['se'],
'ソ' : ['so'],
'ザ' : ['za'],
'ジ' : ['ji'],
'ジェ' : ['jhe','je'],
'ズ' : ['zu'],
'ゼ' : ['ze'],
'ゾ' : ['zo'],
'ン' : ['n']},
#4
{'タ' : ['ta'],
'チ' : ['chi'],
'チェ' : ['chixe','che'],
'ツ' : ['tsu'],
'ッ' : ['xtsu'],
'テ' : ['te'],
'ティ' : ['ti','texe'],
'ト' : ['to'],
'トゥ' : ['tu','toxe'],
'ダ' : ['da'],
'ヂ' : ['di','ji','jhi'],
'ヅ' : ['du','tzu','zu'],
'デ' : ['de'],
'ディ' : ['di','dixe'],
'ド' : ['do'],
'ドゥ' : ['du','duxe']},
#5
{'ナ' : ['na'],
'ニ' : ['ni'],
'ヌ' : ['nu'],
'ネ' : ['ne'],
'ノ' : ['no']},
#6
{'ハ' : ['ha'],
'ヒ' : ['hi'],
'ファ' : ['fa'],
'フィ' : ['fi'],
'フ' : ['fu'],
'フェ' : ['fe'],
'フォ' : ['fo'],
'ヘ' : ['he'],
'ホ' : ['ho'],
'バ' : ['ba'],
'ビ' : ['bi'],
'ブ' : ['bu'],
'ベ' : ['be'],
'ボ' : ['bo'],
'パ' : ['pa'],
'ピ' : ['pi'],
'プ' : ['pu'],
'ペ' : ['pe'],
'ポ' : ['po']},
#7
{'マ' : ['ma'],
'ミ' : ['mi'],
'ム' : ['mu'],
'メ' : ['me'],
'モ' : ['mo']},
#8
{'ヤ' : ['ya'],
'ユ' : ['yu'],
'ヨ' : ['yo']},
 
#9
{'ラ' : ['ra'],
'リ' : ['ri'],
'ル' : ['ru'],
'レ' : ['re'],
'ロ' : ['ro']},
#10
{'ワ' : ['wa'],
'ヲ' : ['wo']},
#11
{'キャ' : ['kya'],
'キュ' : ['kyu'],
'キョ' : ['kyo'],
'ギャ' : ['gya'],
'ギュ' : ['gyu'],
'ギョ' : ['gyo'],
'シャ' : ['sha','shya'],
'シュ' : ['shu','shyu'],
'ショ' : ['sho','shyo'],
'ジャ' : ['jya'],
'ジュ' : ['jyu'],
'ジョ' : ['jyo'],
'チャ' : ['cya','chya','cha'],
'チュ' : ['cyu','chyu','chu'],
'チョ' : ['cyo','chyo','cho'],
'ヒャ' : ['hya'],
'ヒュ' : ['hyu'],
'ヒョ' : ['hyo'],
'ビャ' : ['bya'],
'ビュ' : ['byu'],
'ビョ' : ['byo'],
'ピャ' : ['pya'],
'ピュ' : ['pyu'],
'ピョ' : ['pyo'],
'ミャ' : ['mya'],
'ミュ' : ['myu'],
'ミョ' : ['myo'],
'リャ' : ['rya'],
'リュ' : ['ryu'],
'リョ' : ['ryo']}
]

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
dir_dict={
'1' : ['basic phrases'],
'2' : ['basic vocabulary'],
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
