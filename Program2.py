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


def get_Total_Score (score1):
    total = score1 
    print (f"Your score is: {total}/10. ")



answer1, correct_Answer1 = item1 ()
score1 = check_Item1 ()
get_Total_Score (score1)