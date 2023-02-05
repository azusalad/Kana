import argparse
import time
from config import *
import sys
sys.path.insert(0, 'assets')
from kana_choose import choose_term
from kana_class import kana
from kana_io import readfile, checkpoint, feedback
from kana_modes import flash_check, normal_check

parser = argparse.ArgumentParser()
parser.add_argument("-m", "--mode", required=True, help="Choose flashcard mode or normal mode [flash/normal]")
parser.add_argument("input", help="Kana file to study")
args = parser.parse_args()

if args.mode == "flash":
    flashcard_mode = True
elif args.mode == "normal":
    flashcard_mode = False
else:
    raise Exception("Invalid argument for --mode.  Choose either f or n")
input_file = args.input

# initialize pp and other things
term_dict, pp_dict, wrong_list, file_play = readfile(input_file)
kana_list = []
if pp_dict:
    for term in term_dict:
        # kana(key,values,pp)
        kana_list.append(kana(term,term_dict[term],pp_dict[term]))
else:
    for term in term_dict:
        kana_list.append(kana(term,term_dict[term],0))
        
if not wrong_list:
    wrong_list = []
if not file_play:
    file_play = 0

# main flashcard program
finish = False
time_list = []
session_play = 0
total_correct = 0
combo = 0
easy_list = []
unique_correct = []

while not finish:
    
    # check and let the uesr know if they got everything correct at least once
    if len(unique_correct) == len(kana_list):
        print('You got everything correct at least once')
        # to never show this message again
        unique_correct.append('a')
    
    # choose a kana
    card = choose_term(kana_list, wrong_list, easy_list, session_play+file_play)
    # if everything is in easy list
    if not card:
        print('Everything has been put into the easy list.  Stopping program')
        break
    # print the key
    print(card.key)
    
    # user answers
    time_start = time.time()
    answer = input('>')
    time_end = time.time()
    answer_time = time_start - time_end
    
    if answer != '!quit':
        # get results
        if flashcard_mode:
            result = flash_check(card)
        else:
            result = normal_check(card, answer)
            # add to values if contested answer was correct
            if type(result) == tuple:
                card.values.append(answer)
                result = result[0]
            
        # print feedback
        feedback(card, result)
        
        # add to wrong list if needed else add to correct and unique count
        # if easy then remove from wrong list and add to easy list
        if result == 1:
            wrong_list.append(card)
        else:
            total_correct += 1
            combo += 1
            if card.key not in unique_correct:
                unique_correct.append(card.key)
            if result == 2:
                if card.key in wrong_list:
                    wrong_list.remove(card)
                easy_list.append(card)
            

        # time
        time_list.append(answer_time)
        # find average time
        average_time = 0
        for x in time_list:
            average_time = average_time + x
        average_time = average_time / len(time_list)

        
        # alter pp
        card.alter_pp(result, answer_time, average_time)
        for x in kana_list:
            if x != card:
                x.update_pp()
                
        # alter other stuff
        session_play += 1
        accuracy = total_correct / session_play
        
        # do a checkpoint if needed
        if session_play % checkpoint_turn == 0:
            checkpoint(input_file, kana_list, wrong_list, session_play, session_play+file_play, average_time, combo, accuracy)
        
    else:
        finish = True
        

# when done studying
checkpoint(input_file, kana_list, wrong_list, session_play, session_play+file_play, average_time, combo, accuracy)
print('See you next time')
    
