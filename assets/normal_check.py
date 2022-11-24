# 0 for correct
# 1 for incorrect
# 2 for easy
def normal_check(kana, guess):
    # Checks if the user guess is correct.
    # If not, allow user to contest decision and they can say if they are actually correct
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
        if contest == 'y':
            result = 0
        else:
            result = 1
            
    return result
