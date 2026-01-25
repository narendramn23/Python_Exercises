

def _2_digit_num(num):
    if 10 <= num <= 99:
        print(num, "number is 2 dight number")

def _3_digit_num(num):
    if 100<= num <= 999:
        print( num, "number is 3 dight number")


# main unction 
def performance_check():
    num1 = int(input("enter first number: "))
    num2 = int(input("enter second number: "))
    if 10 <= num1 <= 99:
        _2_digit_num(num1)
    elif 100<= num1 <= 999:
        _3_digit_num(num1)
    else:
        print("number as it is", num1)

    if 10 <= num2 <= 99:
        _2_digit_num(num2)
    elif 100<= num2 <= 999:
        _3_digit_num(num2)
    else:
        print("number as it is", num2)



performance_check()

               
