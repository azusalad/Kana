import random
import re
def turn():
    global win
    global tries
    guess = str(input("Guess a letter or word (no caps).  Type !win to instantly win.\n>"))
    if guess == word:
        win = True
    elif guess == "!win":
        win = True
    else:
        guess_pos = [m.start() for m in re.finditer(guess, word)]
        if len(guess_pos) == 1:
            str_guess_pos = ''.join(str(e) for e in guess_pos)
            word_list[int(str_guess_pos)] = guess
        elif len(guess_pos) == 0:
            wrong_list.append(guess)
        else:
            for x in guess_pos:
                word_list[int(x)] = guess
        print(word_list)
        print("Wrong list:" + str(wrong_list))
    tries = tries + 1
win = 0
tries = 0
wordchoice_list = [
'おはよう',
'こんいちは',
'こんばんは',
'さようなら',
'おやすみ',
'ありがとう',
'すみません',
'いいえ',
'いってきます',
'いってらっしゃい',
'ただいま',
'おかえり',
'いただきます',
'ごちそうさま',
'はじめまして',
'よろしくおねがいします',
'あの',
'いま',
'えいご',
'ええ',
'がくせい',
'こうこう',
'ごご',
'ごぜん',
'せんこう',
'せんせい',
'そうです',
'そうですか',
'だいがく',
'でんわ',
'ともだち',
'なまえ',
'なに',
'にほん',
'はい',
'はん',
'ばんごう',
'りゅうがくせい',
'わたし',
'アメリカ',
'イギリス',
'オーストラリア',
'かんこく',
'スウィーデン',
'ちゅうごく',
'かがく',
'けいざい',
'コンピューター',
'せいじ',
'ビジネス',
'ぶんがく',
'れきし',
'しごと',
'いしゃ',
'かいしゃいん',
'こうこうせい',
'しゅふ',
'だいがくいんせい',
'だいがくせい',
'べんごし',
'おかあさん',
'おとうさん',
'おねえさん',
'おにいさん',
'いもうと',
'おとうと',
'おはようございます',
'おやすみなさい',
'ありがとうございます',
'おかえりなさい',
'ごちそうさまでした']
word = random.choice(list(wordchoice_list))
#print(word)
length = int(len(word)) - 1
#length refers to length of the word minus 1
word_list = ["_"]
wrong_list = []
for i in range(length):
	word_list.append("_")
print(word_list)
while win == False:
    turn()
    if len(word_list) == len(word) and "_" not in word_list:
        break
print("You win!\nThe word was " + str(word) + ".\nIt took you " + str(tries) + " tries.")


	
