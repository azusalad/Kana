import argparse
import random
from config import *
import sys
sys.path.insert(0, '..')
from checkpoint import checkpoint
from feedback import feedback
from flash_check import flash_check
from kanadict import kana
from kanareadfile import readfile
from normal_check import normal_check


parser = argparse.ArgumentParser(description='Kana flashcard program')
parser.add_arguemnt('input_file', type=str, help='Flashcard dictionary file', required=True)
parser.add_argument()
parser.parse_args()

flashcard_mode = True
input_file = 'lmao.txt'

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
correct_count = 0
combo = 0
while not Finish:
    # get a random kana
    card = random.choice(kana_list)
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
            result = normal_check(card)
            
        # print feedback
        feedback(card, correct_text, wrong_text)
        
        # add to wrong list if needed else add to correct count
        if result == 1:
            wrong_list.append(card.key)
        else:
            correct_count += 1
            combo += 1
            

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
        if session_play % 25 == 0:
            checkpoint(input_file, kana_list, wrong_list, session_play, total_play, average_time, combo, accuracy)
        
    else:
        finish = True
        

# when done studying
checkpoint(input_file, kana_list, wrong_list, session_play, total_play, average_time, combo, accuracy)
print('See you next time')
    
