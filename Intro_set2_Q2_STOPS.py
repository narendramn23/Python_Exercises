"""
Using the starting and ending values of your car’s odometer, 
and the measure of fuel consumed, 
calculate the number of stops one should make for refuelling 
while travelling from Bangalore to Goa, 
a distance of 560 kms.

"""
#starting odo meter rading
Initial_reading = int(input("Enter iniitial reading: "))

#ending reading
final_reading = int(input("Enter final reading: "))

#total diatance travelled 
distance_traveled = final_reading - Initial_reading

print("distance traveled:",distance_traveled,"KM")

# what is the fule consumation ?
fuel_consume = int(input("enter fuel consumed to travel: "))

#milage of my car by assuming fuel consumtion
milage = distance_traveled / fuel_consume

print("milage is:", milage,"KM")


tank_capacity = int(input("Enter your vehical fuel tank capacity: "))

#total distance from bangalore to goa
travel_distace = 560

fuel_required = travel_distace / milage

print("fuel_required_to_travel_from_bangalore_to_goa of 560 KM :",fuel_required)

refueling_stops = fuel_required / tank_capacity

print("number_of_stops_to_refueling: ",refueling_stops)


