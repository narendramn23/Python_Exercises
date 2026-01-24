

#if num1 >= 10 and num1 <= 99:
    #print(num1, "is 2 digit number")
    
#if num2 >= 100 and num2 <= 999:
    #print(num2, "is 3 dight number")

#elif (num1 or num2 >= 1000):
    #print("Entered numbers are not correct", num1, num2)

#else:
    #print("entered numebr is negative number , please enter possitive number")
    

def number(num1 = None, num2 = None):

    if len(num1) == 2:
        print(num1,"is 2-digit number")
    elif len(num1) == 3:
        print(num1, " is 3-digit number")
    else:
        print(num1)
    if len(num2) == 2:
        print(num2, "is 2-dight number")
    elif len(num2) == 3:
        print(num2,"is 3-digit number")
    else:
        print(num2)
    while num1 and num2 == None:
        print("please enter num1 and num2")
        continue


num1 = (input("enter first number: "))

num2 = (input("enter second number: "))

        
a = number(num1, num2)

print(a)


def get_number(prompt):
    while True:
        num = input(prompt)
        if num:
            return num
        print("You must enter a number.")

def number(num1, num2):
    if len(num1) == 2:
        print(num1, "is a 2-digit number")
    elif len(num1) == 3:
        print(num1, "is a 3-digit number")
    else:
        print(num1)

    if len(num2) == 2:
        print(num2, "is a 2-digit number")
    elif len(num2) == 3:
        print(num2, "is a 3-digit number")
    else:
        print(num2)

# Repeatedly ask for num1 and num2 until valid input is provided
num1 = get_number("Enter the first number: ")
num2 = get_number("Enter the second number: ")

number(num1, num2)
