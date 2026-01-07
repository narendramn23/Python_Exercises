user_entry = int(input("Enter your number: "))
count = 0

while count < user_entry:
    new_count = str(count)
    print(new_count*(user_entry - 1), end ="")
    count = count + 1 
