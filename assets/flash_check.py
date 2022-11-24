# 0 for correct
# 1 for incorrect
# 2 for easy
def flash_check(kana):
    print('Answer is ' + str(kana.values))
    contest = str(input('Did you get it right? (anything for yes, [n]o, [e]asy)'))
    if contest == 'n':
        return 1
    elif contest == 'e':
        return 2
    else:
        return 0
    
