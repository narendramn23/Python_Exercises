'''
Print multiplication table
user choice

'''
# using while loop
number = int(input("enter which table you need: "))
count = 1
while count < 11:
    ans = number * count
    print(number, "X", count, "=", ans)
    count = count + 1


#using for loop

for num in range (1, 11):
    ans = number * num
    print(number, "X", num, "=", ans)
    
