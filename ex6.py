#!/usb/bin/python

# Set a variable named x that contains a sentence with an integer variable in it.
x = "There are %d types of people." % 10

# Set a variable named binary that is a string: "binary"
binary = "binary"

# Set a variable named do_not that is a string "don't"
do_not = "don't"

# Set a variable y that is a string made of a sentence with two variables, binary and do_not
y = "Those who know %s and those who %s." % (binary, do_not)

# Print variable "x"
print x

# Print variable "y"
print y

# Print variable x as part of a string using the %r method.
print "I said: %r." % x 

# Print varialbe y as a string input into a string.
print "I also said: '%s'." % y

# Set a variable that is the boolean reserved word "False", not a string
hilarious = False

# Set a variable joke_evaluation and concat a string/sentence and pull in hilarious using %r
joke_evaluation = "Isn't that joke so funny?! %r"

# Print joke evaulation but pull in hilarious as the variable for the %r in joke_evaluation
print joke_evaluation % hilarious

# Set a variable w that is a string
w = "This is the left side of..."

# Set a varialble e that is a string
e = "a string with a right side."

# Print w and e as a concat using the "+" symbol
print w + e
