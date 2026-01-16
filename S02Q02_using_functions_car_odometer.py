def odo_meter(start,end,fuel):

    total_distance = end - start
    milage = total_distance // fuel

    return milage



         
if __name__ == "__main__":
    print("main task",__name__)
    start = float(input("enter starting distance: "))
    end = float(input("enter end distance: "))
    fuel =float(input("enter fuel consumed : "))

    odo = odo_meter(start,end,fuel)
    print("milage of your car is ",odo)
