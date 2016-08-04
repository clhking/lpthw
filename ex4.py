# Set a variable for the number of cars
cars = 100
# Set a variable (using a float) for space in each car
space_in_a_car = 4
# Set a variable with number of drivers
drivers = 30
# Set a variable with number of passengers
passengers = 90
# Set up the variable for cars not driven being # of cars minus number of drivers
cars_not_driven = cars - drivers
# set a variable cars = drivers # this could be wrong in the future, there should be a check for cars gte drivers
cars_driven = drivers
# setup carpool_capacity being space in cars multiplied by cars_driven
carpool_capacity = cars_driven * space_in_a_car 
# setup avg_pass_per_car as being passengers divided by cars_driven
average_passengers_per_car = passengers / cars_driven

# print out number of cars    
print "There are", cars, "cars available."
# print out number of drivers
print "There are only", drivers, "drivers available."
# print out number of cars not driven
print "There will be", cars_not_driven, "empty cars today."
# print out the carpool capacity
print "We can transport", carpool_capacity, "people today."
# print out number of passengers
print "We have", passengers, "to carpool today."
# print out avg # of passengers per car
print "We need to put about", average_passengers_per_car, "in each car." 

