def readfile(desired_file):
    '''
    loads a file containing flashcard information
    outputs a tuple
    '''
    import ast
    
    f = open(desired_file,'r')
    file_index = [x for x in f.readlines() if x != '']
    f.close()
    
    # index 0 is term_dict
    # index 1 is pp_dict
    # index 2 is wrong_list
    # index 3 is playtime 
    
    # get term dictionary
    data = []
    data.append(ast.literal_eval(file_index[0]))
    if len(file_index) > 1:
        # get pp dictionary if exists
        data.append(ast.literal_eval(file_index[1]))
        if len(file_index) > 2:
            # get wrong list if exists
            data.append(ast.literal_eval(file_index[2]))
            if len(file_index) > 3:
                # get playtime if exists
                data.append(int(ast.literal_eval(file_index[3])))
    
    # add false to remaining items in list if things dont exist
    while len(data) < 4:
        data.append(False)
        
    return tuple(data)
    


def checkpoint(input_file, kana_list, wrong_list, session_play, total_play, average_time, combo, accuracy):
    # Writes to file, prints rank and pp
    
    import os
    
    # make term and pp dict
    term_dict = {}
    pp_dict = {}
    for x in kana_list:
        term_dict[x.key] = x.values
        pp_dict[x.key] = x.pp
        
    # write to file
    f = open(input_file, 'w', encoding="utf-8")
    f.write(str(term_dict))
    f.write('\n')
    f.write(str(pp_dict))
    f.write('\n')
    f.write(str([x.key for x in wrong_list]))
    f.write('\n')
    f.write(str(session_play + total_play))
    f.close()
    
    # print rank pictures
    if accuracy == 100:
        rank = "SS"
        os.system('kitty +kitten icat ../ranks/ranking-x@2x.png')
    elif accuracy >= 95:
        rank = "S"
        os.system('kitty +kitten icat ../ranks/ranking-s@2x.png')
    elif accuracy >= 90:
        rank = "A"
        os.system('kitty +kitten icat ../ranks/ranking-a@2x.png')
    elif accuracy >= 80:
        rank = "B"
        os.system('kitty +kitten icat ../ranks/ranking-b@2x.png')
    elif accuracy >= 70:
        rank = "C"
        os.system('kitty +kitten icat ../ranks/ranking-c@2x.png')
    elif accuracy >= 60:
        rank = "D"
        os.system('kitty +kitten icat ../ranks/ranking-d@2x.png')
    else:
        rank = "F (you suck lmao)"
        os.system('kitty +kitten icat ../ranks/section-fail@2x.png')
        
    # print some text
    print(
        "\nYou have played " + str(session_play) + " times since Kana started!\nAverage time: " + str(average_time) + " Combo: " + str(combo) + " Accuracy: " + str(
            accuracy) + " Rank: " + str(rank))
    print('Performance Points: ' + str(pp_dict) + '\n')

# 0 for correct
# 1 for incorrect
# 2 for easy
def feedback(kana, result, correct_text, wrong_text):
    """
    Prints the feedback of the result
    Like telling the user if they got it right
    """
    
    # incorrect
    if result == 1:
        print(str(wrong_text) + str(kana.values))
        
    # correct/easy
    elif result == 1:
        print(str(correct_text) + str(kana.values))
