name = input("enter your name : ")
surname = input("enter your surname :")

print("Name:",name,","+"Surename:",surname)

print(name.upper() +" " + surname.upper())

print("="* 30)

c =(name.replace(name, surname).capitalize() + "," + surname.replace(surname, name).capitalize())

print(c)


def myname(name, surname):
    a = "Name:",name,","+"Surename:",surname
    b = name.upper() +" " + surname.upper()
    c = "="* 30
    d = name.replace(name, surname).capitalize() + "," + surname.replace(surname, name).capitalize()
    return a, b, c, d

# main start from here

a = input("enter your name : ")
b = input("enter your surname :")
z,x,c,d = myname(a, b)

print(z)
print(x)
print(c)
print(d)












