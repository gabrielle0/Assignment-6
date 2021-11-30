#Steps: 
#Step 1:Create a program that ask for 4 numbers. 
#Step 2:Print the 4 numbers from highest to lowest using only if-else statement.

def enter_4_Numbers ():
    first_Input = int (input (f"Give 1st number: "))
    second_Input  = int (input (f"Give 2nd number: "))
    third_Input = int (input (f"Give 3rd number: "))
    fourth_Input = int (input (f"Give 4th number: "))
    return first_Input, second_Input, third_Input, fourth_Input

def get_First (first_Input, second_Input, third_Input, fourth_Input):
    if first_Input > second_Input and first_Input > third_Input and first_Input > fourth_Input:
        first = first_Input
    else:
        if second_Input > first_Input and second_Input > third_Input and second_Input > fourth_Input:
            first = second_Input
        else:
            if third_Input > first_Input and third_Input > second_Input and third_Input > fourth_Input:
                first = third_Input
            else:
                fourth_Input > first_Input and fourth_Input > second_Input and fourth_Input > third_Input
                first = fourth_Input
    return first

def get_Second (first_Input, second_Input, third_Input, fourth_Input, first, fourth):
    if  first > first_Input > fourth and (first_Input > second_Input > fourth or first_Input > third_Input > fourth or first_Input > fourth_Input > fourth):
        second = first_Input
    else:
        if first > second_Input > fourth and (second_Input > first_Input > fourth or second_Input > third_Input > fourth or second_Input > fourth_Input > fourth):
            second = second_Input
        else:
            if first > third_Input > fourth and (third_Input > first_Input > fourth or third_Input > second_Input > fourth or third_Input > fourth_Input > fourth):
                second = third_Input
            else:
                first > fourth_Input > fourth and (fourth_Input > first_Input > fourth or fourth_Input > second_Input > fourth or fourth_Input > third_Input > fourth)
                second = fourth_Input
    return second 

def get_Third (first_Input, second_Input, third_Input, fourth_Input, first, second, fourth):
    if first > second > first_Input > fourth:
        third = first_Input
    else:
        if first > second > second_Input > fourth:
            third = second_Input
        else:
            if first > second > third_Input > fourth:
                third = third_Input
            else:
                first > second > fourth_Input > fourth
                third = fourth_Input
    return third

def get_Fourth (first_Input, second_Input, third_Input, fourth_Input):
    if first_Input < second_Input and first_Input < third_Input and first_Input < fourth_Input:
        fourth = first_Input
    else:
        if second_Input < first_Input and second_Input < third_Input and second_Input < fourth_Input:
            fourth = second_Input
        else:
            if third_Input < first_Input and third_Input < second_Input and third_Input < fourth_Input:
                fourth = third_Input
            else:
                fourth_Input < first_Input and fourth_Input < second_Input and fourth_Input < third_Input
                fourth = fourth_Input
    return fourth



first_Input, second_Input, third_Input, fourth_Input = enter_4_Numbers ()
first = get_First (first_Input, second_Input, third_Input, fourth_Input)
fourth = get_Fourth (first_Input, second_Input, third_Input, fourth_Input)
second = get_Second (first_Input, second_Input, third_Input, fourth_Input, first, fourth)
third = get_Third (first_Input, second_Input, third_Input, fourth_Input, first, second, fourth)

print (f"The numbers arranged from highest to lowest are: {first}, {second}, {third}, {fourth}")


