def num(user_num):
    if len(user_num) == 1:
        user_num = int(user_num) + 7
        user_num = str(user_num)
        a = user_num
        print("Number in unit pleace is ", a[-1:])
    
    elif len(user_num) == 2:
        user_num = int(user_num)**5
        user_num = str(user_num)
        b = user_num
        print("Last 2 digits are :", b[-2:])

    elif len(user_num) == 3:
        new_num = input("Enter another number:", )
        c = int(user_num) + int(new_num)
        c = str(c)
        print("Last 3 digit number: ", c[-3:])



#main starts form here
if __name__ == "__main__":
    print("This is main function", __name__)
    user_num = input("Enter number :")
    num(user_num)

