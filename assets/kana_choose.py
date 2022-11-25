def choose_term(kana_list, wrong_list, easy_list, total_play):
    # Choose a term from the kana list depending on the performance
    
    import random
    
    pool = []
    for x in kana_list:
        if x not in easy_list:
            pool.append(x)
            
    rank_start = int(round(len(kana_list) * 0.5))
    if total_play > rank_start and total_play % 5 == 0 and wrong_list:
        card = random.choice(wrong_list)
        print('Showing term from wrong list:')
    elif total_play > rank_start and total_play % 2 == 0:
        worst_pp = pool[0].pp
        for x in pool:
            if x.pp > worst_pp:
                worst_pp = x.pp  # looks through all of the values in pp_dict and determines the worst pp
        for x in pool:
            if x.pp == worst_pp:
                card = x
                print('Showing term based off rank: ' + str(worst_pp))
                break
    elif len(pool) == 0:
        print('Everything is in the easy list')
        return False
    else:
        card = random.choice(pool)

    return card
