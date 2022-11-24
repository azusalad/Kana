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
