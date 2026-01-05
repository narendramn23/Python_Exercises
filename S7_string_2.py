first_name = "narendra"
surname = "singh"

while len(first_name) > 4 or len(surname) > 1:
    if len(first_name) == 8:
        print(first_name + " "+  surname)
    if len(first_name) > 4:
        first_name = first_name[:-1]
    if len(surname) > 1:
        surname = surname[:-1]
    print(first_name, surname)
            
print('Best possible initials of narendra singh is:', first_name,surname) 
