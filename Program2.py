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
    if answer1 == correct_Answer1:
        score1 = 1
    else:
        score1 = 0
    return answer1, correct_Answer1, score1

def item2 ():
    given1 = random.randint (0, 99)
    given2 = random.randint (0, 99) 
    answer2 = int (input (f"{given1} + {given2} = "))
    correct_Answer2 = given1 + given2
    if answer2 == correct_Answer2:
        score2 = 1
    else:
        score2 = 0
    return answer2, correct_Answer2, score2

def item3 ():
    given1 = random.randint (0, 99)
    given2 = random.randint (0, 99) 
    answer3 = int (input (f"{given1} + {given2} = "))
    correct_Answer3 = given1 + given2
    if answer3 == correct_Answer3:
        score3 = 1
    else:
        score3 = 0
    return answer3, correct_Answer3, score3

def item4 ():
    given1 = random.randint (0, 99)
    given2 = random.randint (0, 99) 
    answer4 = int (input (f"{given1} + {given2} = "))
    correct_Answer4 = given1 + given2
    if answer4 == correct_Answer4:
        score4 = 1
    else:
        score4 = 0
    return answer4, correct_Answer4, score4

def item5 ():
    given1 = random.randint (0, 99)
    given2 = random.randint (0, 99) 
    answer5 = int (input (f"{given1} + {given2} = "))
    correct_Answer5 = given1 + given2
    if answer5 == correct_Answer5:
        score5 = 1
    else:
        score5 = 0
    return answer5, correct_Answer5, score5

def item6 ():
    given1 = random.randint (0, 99)
    given2 = random.randint (0, 99) 
    answer6 = int (input (f"{given1} + {given2} = "))
    correct_Answer6 = given1 + given2
    if answer6 == correct_Answer6:
        score6 = 1
    else:
        score6 = 0
    return answer6, correct_Answer6, score6

def item7 ():
    given1 = random.randint (0, 99)
    given2 = random.randint (0, 99) 
    answer7 = int (input (f"{given1} + {given2} = "))
    correct_Answer7 = given1 + given2
    if answer7 == correct_Answer7:
        score7 = 1
    else:
        score7 = 0
    return answer7, correct_Answer7, score7

def item8 ():
    given1 = random.randint (0, 99)
    given2 = random.randint (0, 99) 
    answer8 = int (input (f"{given1} + {given2} = "))
    correct_Answer8 = given1 + given2
    if answer8 == correct_Answer8:
        score8 = 1
    else:
        score8 = 0
    return answer8, correct_Answer8, score8

def item9 ():
    given1 = random.randint (0, 99)
    given2 = random.randint (0, 99) 
    answer9 = int (input (f"{given1} + {given2} = "))
    correct_Answer9 = given1 + given2
    if answer9 == correct_Answer9:
        score9 = 1
    else:
        score9 = 0
    return answer9, correct_Answer9, score9

def item10 ():
    given1 = random.randint (0, 99)
    given2 = random.randint (0, 99) 
    answer10 = int (input (f"{given1} + {given2} = "))
    correct_Answer10 = given1 + given2
    if answer10 == correct_Answer10:
        score10 = 1
    else:
        score10 = 0
    return answer10, correct_Answer10, score10

def get_Total_Score (score1, score2, score3, score4, score5, score6, score7, score8, score9, score10 ):
    total = score1 + score2 + score3 + score4 + score5 + score6 + score7 + score8 + score9 + score10
    print (f"Your score is: {total}/10. ")


answer1, correct_Answer1,score1 = item1 ()
answer2, correct_Answer2, score2 = item2 ()
answer3, correct_Answer3, score3 = item3 ()
answer4, correct_Answer4, score4 = item4 ()
answer5, correct_Answer5, score5 = item5 ()
answer6, correct_Answer6, score6 = item6 ()
answer7, correct_Answer7, score7 = item7 ()
answer8, correct_Answer8, score8 = item7 ()
answer9, correct_Answer9, score9 = item7 ()
answer10, correct_Answer10, score10 = item7 ()

get_Total_Score (score1, score2, score3, score4, score5, score6, score7, score8, score9, score10)

