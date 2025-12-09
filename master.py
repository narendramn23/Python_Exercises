def divide(num, din):
    quot = num // din
    rem = num % din
    return quot, rem
    
total = 10000
effort = 3

days, hrs = divide(total, effort)

month,days = divide(days, 30)

years, month = divide(month, 12)

print(years, "yrs", month, "months", days, "days", hrs, "hrs")

