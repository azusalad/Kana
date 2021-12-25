# Version 20210426 added '' as an answer for contest
import random
import time
import wx
import ast

def get_path(wildcard):
    app = wx.App(None)
    style = wx.FD_OPEN | wx.FD_FILE_MUST_EXIST
    dialog = wx.FileDialog(None, 'Choose a dictionary', wildcard=wildcard, style=style)
    if dialog.ShowModal() == wx.ID_OK:
        path = dialog.GetPath()
    else:
        path = None
    dialog.Destroy()
    return path
# opens a gui thing that allows you to choose a file

print('Choose a dictionary')
file_path = get_path('*.txt')
f = open(file_path, "r",encoding='utf8')
file_index = f.read().split("\n")
f.close()
"""
opens the file you chose and puts every line as an item in a list
indices:
0: term dictionary
1: pp dictionary
2: wrong list
3: turn number
"""

old_dict = ast.literal_eval(file_index[0])
term_dict = old_dict.copy()
flashcard_mode = int(input('Enable flashcard mode?  1 for yes'))
# flashcard mode is the exact same as regular mode except you dont have to type.  good for terms with long definitions
if flashcard_mode == 1:
    flashcard_mode = True
else:
    flashcard_mode = False

try:
    file_index[1]
except:
    pp_dict = term_dict.copy()
    for x in term_dict:
        pp_dict[x] = 0  # creates pp_dict with all values starting at 0.  Higher values means terms you are worse at.
else:
    pp_dict = ast.literal_eval(file_index[1])
    print("Retrieved old performance")
finally:
    pass
try:
    file_index[2]
except:
    wrong_list = []
else:
    wrong_list = ast.literal_eval(file_index[2])
    print('Retrieved old wrong list')
finally:
    pass
try:
    file_index[3]
except:
    fileplay = 0
else:
    fileplay = int(ast.literal_eval(file_index[3]))
    print('Retrieved old playtime')
finally:
    pass
# this entire thing retrieves old stats

combo = 0
sessionplay = 0
totalcorrect = 0
finish = False
time_list = []  # this list will contain all the values for time that it took you to answer the key
totalplay = fileplay + sessionplay
average_time = 0
rank_start = int(round(len(term_dict) * 0.5))  # this is a weighed value on when to start showing terms based on pp
print('Will start showing terms based on rank on overall turn ' + str(rank_start) + '.  Total number of terms: ' + str(len(term_dict)))

pp_correct = 7    # -
pp_wrong = 9      # +
pp_05bonus = 7    # -
pp_15penalty = 1  # +
pp_2penalty = 2   # +
pp_inactive = 4   # +
# for quick adjustment of pp adjustments

def printstatus():
    if accuracy == 100:
        rank = "SS"
    elif accuracy >= 95:
        rank = "S"
    elif accuracy >= 90:
        rank = "A"
    elif accuracy >= 80:
        rank = "B"
    elif accuracy >= 70:
        rank = "C"
    elif accuracy >= 60:
        rank = "D"
    else:
        rank = "F (you suck lmao)"
    print(
        "\nYou have played " + str(sessionplay) + " since flashcards started!\nAverage time: " + str(average_time) + " Combo: " + str(combo) + " Accuracy: " + str(
            accuracy) + " Rank: " + str(rank))
    print('Performance Points: ' + str(pp_dict) + '\n')

def correct_answer():
    global combo
    global totalcorrect
    global pp_dict
    global key
    global correct
    global flashcard_mode
    combo = combo + 1
    if not flashcard_mode:
        print("Correct " + str(value))
    totalcorrect = totalcorrect + 1
    if combo % 10 == 0:
        print("Combo: " + str(combo))
    pp_dict[key] = pp_dict[key] - pp_correct
    correct = True

def file_update():
    totalplay = sessionplay + fileplay
    with open(file_path, 'w', encoding="utf-8") as f:
        #f = open(file_path, "w")
        f.write(str(old_dict) + '\n' + str(pp_dict) + '\n' + str(wrong_list) + '\n' + str(totalplay))
    #f.close()
# saves stats

while not finish:
    totalplay = fileplay + sessionplay
    if totalplay > rank_start and totalplay % 5 == 0 and wrong_list: # shows a term from the wrong list
        key = random.choice(wrong_list)
        print('Showing term from wrong list:')
    elif totalplay > rank_start and totalplay % 2 == 0:  # starts showing based off of pp after the weighted rank_start value.  Also only shows a pp term every third iteration
        worst_pp = 0
        for x in pp_dict:
            if pp_dict[x] > worst_pp:
                worst_pp = pp_dict[x]  # looks through all of the values in pp_dict and determines the worst pp
        for x in pp_dict:
            if pp_dict[x] == worst_pp:
                for k in term_dict:
                    if x == k:
                        key = k  # finds the first term in term_dict that has a value matching worst pp
                        print('Showing term based off rank: ' + str(worst_pp))
                        break
                break
    else:
        key = random.choice(list(term_dict))  # regular key choosing

    value = term_dict[key]
    print(key)
    time_start = time.time()
    answer = input('>')
    time_end = time.time()
    answer_time = time_end - time_start  # this calculates the time it took to answer the key
    if answer in value:  # default correct
        correct_answer()
    elif answer == "!quit":  # quits program
        finish = True
        break
    else:
        if not flashcard_mode:
            print("dumbass the real answer is '" + str(value) + "'\nCombo: " + str(combo))
        else:
            print('Answer is ' + str(value))
        if not flashcard_mode:
            contest = str(input("contest? "))
        else:
            contest = str(input('Did you get it right? '))
        if contest == "1" or contest == "y" or contest == "":  # you got it wrong but you can contest the answer
            correct_answer()
            if not flashcard_mode:
                term_dict[key].append(answer) # smart learning
        else:  # you said you really got it wrong
            combo = 0
            pp_dict[key] = pp_dict[key] + pp_wrong
            wrong_list.append(key) # always appends if you get it wrong so program will have a higher chance of choosing something that you get wrong often when it picks from the wrong list
            correct = False

    # finally:
    time_list.append(answer_time)
    average_time = 0
    for x in time_list:  # finds average time
        average_time = average_time + x
    average_time = average_time / len(time_list)

    if sessionplay > rank_start:  # pp adjustment depending on time it took to answer
        if answer_time < 0.5 * average_time and correct == True:
            pp_dict[key] = pp_dict[key] - pp_05bonus
        elif answer_time > 1.5 * average_time:
            pp_dict[key] = pp_dict[key] + pp_15penalty
        elif answer_time > 2 * average_time:
            pp_dict[key] = pp_dict[key] + pp_2penalty
    for x in pp_dict:  # pp adjustment for inactive keys
        if x != key:
            pp_dict[x] = pp_dict[x] + pp_inactive

    sessionplay = sessionplay + 1
    accuracy = totalcorrect / sessionplay * 100
    if sessionplay % 25 == 0:
        printstatus()
        file_update()

printstatus()
file_update()
print("See you next time.")
