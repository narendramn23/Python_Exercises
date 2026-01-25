
def do_1digit_oper(num):
    ans1 = (num + 7) % 10
    print(num, "is Singel digit number and result is", ans1)

def do_2digit_oper(num):
    ans2 = (num ** 5) % 10
    print(num, "is double digit number and result is", ans2)

def do_3digit_oper(num):
    num1 = int(input("enter number again: "))
    ans3 = (num1 + num) % 10
    print(num, "is three digit number and result is", ans3)




# Mian function start here 

def perform_check():
    num = int(input("enter number : "))
    
    if 0 < num < 10:
        do_1digit_oper(num)

    elif 10 <= num <= 99:
        do_2digit_oper(num)

    elif 100 <= num <=999:
        do_3digit_oper(num)


perform_check()

    

    


      

    
    



    
###############################################
