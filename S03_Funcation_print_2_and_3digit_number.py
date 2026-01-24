

def find_num(num1,num2):
    if len(num1) == 2:
        print(num1, "is 2 digit number")
    elif len(num1) == 3:
        print(num1, "is 3 digit number")
    else:
        print("printing as it is", num1)
    
    if len(num2) == 2:
        print(num2, "is 2 digit number")
    elif len(num2) == 3:
        print(num2, "is 2 digit number")
    else:
        print("printing as it is", num2)   



if __name__ == "__main__":
    print("main test function call",__name__)

    num1 = input("enter your first number: ")
    num2 = input("enter your second number: ")

    find_num(num1,num2)
    
