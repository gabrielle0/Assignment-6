
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




a, b, c, d = enter_4_Numbers ()
first = arrange (a,b,c,d)





a, b, c, d = enter_4_Numbers ()



#Steps: 
#Step 1:Create a program that ask for 4 numbers. 
#Step 2:Print the 4 numbers from highest to lowest using only if-else statement.