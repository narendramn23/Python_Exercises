def tables():
    use_input = int(input("enter which table you want: "))
    for num in range(1, 11):
         ans = num * use_input
         print(use_input, "X",  num, "=", ans)
