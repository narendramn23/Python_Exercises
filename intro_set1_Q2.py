
'''
This program prints tables with user choice  

'''
user_choice = int(input("Please enter which tables you want : "))

for multiples in range (1, 11):

    answer = user_choice * multiples


    print(user_choice, "X", multiples, "=" ,answer)
