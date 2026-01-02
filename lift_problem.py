
weight = [64, 80, 20, 110, 75, 35, 94, 70, 45, 65]
total_weight = 0
num_people = 0
for i in weight:
    if total_weight + i <= 400:
        total_weight = total_weight + i
        num_people = num_people + 1
    else:
        print("capacity Exceds")
        break
print("number of people enter in to lift for first:", num_people)












        
    
