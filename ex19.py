#!/usr/bin/python

# create a function called cheese and crackers that takes in two arguments
# and creates two variables for them, "cheese_count" and "boxes_of_crackers"
# the function takes in the numbers and then does some print statements
# with them.
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print "You have %d cheeses!" % cheese_count
    print "You have %d boxes of crackers!" % boxes_of_crackers
    print "Man that's enough for a party!"
    print "Get a blanket.\n"


print "We can just give the function numbers directly:"
# call cheese and crackers with two integers staticly input
cheese_and_crackers(20, 30)

print "OR, we can use variables from our script:"
# create variable for the amount of cheese
amount_of_cheese = 10
# create variable for amount of crackers
amount_of_crackers = 50

# call cheese and crackers using the variables you created instead 
# of using staticly entered integers
cheese_and_crackers(amount_of_cheese, amount_of_crackers)


print "We can even do math inside too:"
# call cheese and crackers with math as the input arguments
# python will do the math and then pass the results as the arguments
cheese_and_crackers(10 + 20, 5 + 6)


print "And we can combine the two variables and math:"
# call cheese and crackers using both variables and adding an integer
# for each of the arguments
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)

# Let's ask for the number of cheeses and crackers available.
user_input_cheese = int(raw_input("How many pieces of cheese do you have? > "))
user_input_crackers = int(raw_input("How many boxes of crackers do you have? > "))
cheese_and_crackers(user_input_cheese, user_input_crackers)
