#Steps:
#Step 1: Create a program that automatically generate two random numbers to add (0 to 99).
#Step 2: Let the user answer and evaluate if the user has the correct answer.
#Step 3: The program will ask the user 10 addition operations.
#Step 4: Display the result summary of the 10 operations (ex 9/10).


import random

def item1 ():
    given1 = random.randint (0, 99)
    given2 = random.randint (0, 99) 
    answer1 = int (input (f"{given1} + {given2} = "))
    correct_Answer1 = given1 + given2
    return answer1, correct_Answer1

def check_Item1 ():
    if answer1 == correct_Answer1:
        score1 = 1
    else:
        score1 = 0
    return score1

def item2 ():
    given1 = random.randint (0, 99)
    given2 = random.randint (0, 99) 
    answer2 = int (input (f"{given1} + {given2} = "))
    correct_Answer2 = given1 + given2
    return answer2, correct_Answer2

def check_Item2 ():
    if answer2 == correct_Answer2:
        score2 = 1
    else:
        score2 = 0
    return score2

def item3 ():
    given1 = random.randint (0, 99)
    given2 = random.randint (0, 99) 
    answer3 = int (input (f"{given1} + {given2} = "))
    correct_Answer3 = given1 + given2
    return answer3, correct_Answer3

def check_Item3 ():
    if answer3 == correct_Answer3:
        score3 = 1
    else:
        score3 = 0
    return score3

def item4 ():
    given1 = random.randint (0, 99)
    given2 = random.randint (0, 99) 
    answer4 = int (input (f"{given1} + {given2} = "))
    correct_Answer4 = given1 + given2
    return answer4, correct_Answer4

def check_Item4 ():
    if answer4 == correct_Answer4:
        score4 = 1
    else:
        score4 = 0
    return score4





def get_Total_Score (score1, score2, score3, score4 ):
    total = score1 + score2 + score3 + score4
    print (f"Your score is: {total}/10. ")


answer1, correct_Answer1 = item1 ()
score1 = check_Item1 ()

answer2, correct_Answer2 = item2 ()
score2 = check_Item2 ()

answer3, correct_Answer3 = item3 ()
score3 = check_Item3 ()

answer4, correct_Answer4 = item4 ()
score4 = check_Item4 ()






get_Total_Score (score1, score2, score3, score4)

