# 0 for correct
# 1 for incorrect
# 2 for easy
def feedback(kana, result, correct_text, wrong_text):
    # Prints the feedback of the result
    # Like telling the user if they got it right
    
    # incorrect
    if result == 1:
        print(str(wrong_text) + str(kana.values))
        
    # correct/easy
    elif result == 1:
        print(str(correct_text) + str(kana.values))
