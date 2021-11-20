
def enter_4_Numbers ():
    a = int (input (f"Give 1st number: "))
    b = int (input (f"Give 2nd number: "))
    c = int (input (f"Give 3rd number: "))
    d = int (input (f"Give 4th number: "))
    return a, b, c, d

def arrange (a,b,c,d):
    if a > b > c > d:
        first = a 
    else:
        if b > a > c > d:
            first = b
        else:
            if c > a > b > d:
                first = c
            else:
                d > a > b > c
                first = d
    return first

def arrange2 (a,b,c,d):
    if a < b < c < d:
        fourth = a 
    else:
        if b < a < c < d:
            fourth = b
        else:
            if c < a < b < d:
                fourth = c
            else:
                d < a < b < c
                fourth = d
    return fourth

def arrange3 (a,b,c,d, first, fourth):
    if  first > a > fourth and a > b > fourth or a > c > fourth or a > d > fourth:
        second = a 
    else:
        if first > b > fourth and b > a > fourth or b > c > fourth or b > d > fourth:
            second = b 
        else:
            if first > c > fourth and c > a > fourth or c > b > fourth or c > d > fourth:
                second = c
            else:
                first > d > fourth and d > a > fourth or d > c > fourth or d > b > fourth
                second = d
    return second


def arrange4 (a,b,c,d, first, fourth, second):
    if first > second > a > fourth:
        third = a 
    else:
        if first > second > b > fourth:
            third = b 
        else: 
            if first > second > c > fourth:
                third = c 
            else:
                first > second > d > fourth
                third = d 
    return third


a, b, c, d = enter_4_Numbers ()
first = arrange (a,b,c,d)
fourth = arrange2 (a,b,c,d)
second = arrange3 (a,b,c,d, first, fourth)
third = arrange4 (a,b,c,d, first, second, fourth)

print (f"The numbers arranged from highest to lowest are: {first}, {second}, {third}, {fourth}")


#Steps: 
#Step 1:Create a program that ask for 4 numbers. 
#Step 2:Print the 4 numbers from highest to lowest using only if-else statement.