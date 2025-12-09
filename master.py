total = 10000
#effort = 3
effort = int(input("what is your daily effort ? "))

days = total // effort
rem_hrs = total % effort
month  = days // 30 
rem_days  = days % 30
years = month // 12
rem_month = month % 12

print(years, "yrs", rem_month, "months", rem_days, "days", rem_hrs, "hrs")


#######
