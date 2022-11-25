# 0 for correct
# 1 for incorrect
# 2 for easy
def flash_check(kana):
    """Checks if the user got it correct using the flash card mode."""
    print('Answer is ' + str(kana.values))
    contest = str(input('Did you get it right? (anything for yes, [n]o, [e]asy)'))
    if contest == 'n':
        return 1
    elif contest == 'e':
        return 2
    else:
        return 0
    
def normal_check(kana, guess):
    """
    Checks if the user guess is correct.
    If not, allow user to contest decision and they can say if they are actually correct.
    """
    result = None
    
    # first check if they are correct
    for x in kana.values:
        if str(guess) == str(x):
            result = 0
            # now ask if it is too easy
            easy = str(input("too easy?  (anything for no, [y]es)"))
            if easy == 'y':
                result = 2
    
    # they are not correct, allow them to contest
    if result != 0:
        contest = str(input("contest? ([y]es, anything for no)"))
        # will add to the kana's values if the contested answer is correct
        if contest == 'y':
            return(0,guess)
        else:
            result = 1
            
    return result 
