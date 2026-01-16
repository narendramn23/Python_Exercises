from S02Q02_using_functions_car_odometer import odo_meter

def refuel(tank_capacity,distance = 560):
    
    #re using odo_meter function which i have written previously to calculate milage
    milage = odo_meter(start,end,fuel)
    fuel_required = distance / milage
    refueling_stops = fuel_required / tank_capacity

    return refueling_stops
    



         
if __name__ == "__main__":
    print("main task",__name__)
    start = float(input("enter starting distance: "))
    end = float(input("enter end distance: "))
    fuel = float(input("enter fuel consumed : "))
    tank_capacity = float(input("enter fuel tank capacity: "))

    number_of_stops = refuel(tank_capacity)

    print(" number stops needed to refuel is : ", number_of_stops)
    
