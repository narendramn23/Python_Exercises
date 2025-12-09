total = 10000
effort = 3

days  = total // effort
hrs   = total % effort

month = days // 30 
days  = days % 30

years = month // 12
month = month % 12

print(years, "yrs", month, "months", days, "days", hrs, "hrs")


#function divide(num, den)
#   quot = num / den
#   rem = num % den
#   return quot, rem

#total = 10000
#effort = 3

#days, hrs = divide(total, effort)
#month, days = divide(days, 30 )
#years, month = divide(month, 12 )
