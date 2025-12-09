def divide(num, din):
    quot = num // din
    rem = num % din
    return quot, rem
    
total = 10000
effort = 3

#days = total // effort
#rem_hrs = total % effort
days, hrs = divide(total, effort)

#month  = days // 30 
#days  = days % 30
month,days = divide(days, 30)

#years = month // 12
#month = month % 12
years, month = divide(month, 12)


print(years, "yrs", month, "months", days, "days", hrs, "hrs")
