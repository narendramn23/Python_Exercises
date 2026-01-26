def ethonal_capacity(tank_capacity, current_level):
    
    ethonal_percent = (current_level/tank_capacity) * 100

    if ethonal_percent > 80:
        print('ALARM :'"Ethonal capacity is more then 80% please close the valve")
    elif ethonal_percent < 20:
        print('SMS:'"Ethonal capacity is less then 20% please Buy more ethonal")
    else:
        print("tank is normal")

if __name__ == "__main__":
    print("main function:", __name__)
    
    tank_capacity = 900
    current_level = float(input("Please enter current level of ethanol in the tank in Ltr: "))
    ethonal_capacity(tank_capacity, current_level)
    

    

    
    
        
