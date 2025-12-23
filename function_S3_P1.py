
##### function to get 2 digit and 3 digit number#
def find(number):
    if number >=10 and number <=99:
        print(number ,"2 digit number")
    elif number >= 100 and number <=999:
        print(number, "3 digit number")
    else:
        print(number," not 2 or 3 digit")


def main():
    num1 = int(input (" enter number1 :"))
    num2 = int(input(" enter numbe2 : "))
    find(num1)
    find(num2)


main()







