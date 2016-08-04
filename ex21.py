#!/usr/bin/python

def add(a, b):
    print "ADDING %d + %d" % (a, b)
    return a + b

def subtract(a, b):
    print "SUBTRACTING %d - %d" % (a, b)
    return a - b

def multiply(a, b):
    print "MULTIPLYING %d * %d" % (a, b)
    return a * b

def divide(a, b):
    print "DIVIDING %d / %d" % (a, b)
    return a / b

def what():
    what_divide = divide(iq, 2)
    what_multiply = multiply(weight, what_divide)
    what_subtract = subtract(height, what_multiply)
    what_add = add(age, what_subtract)
    return what_add

print "Let's do some math with just functions!"

age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

print "Age: %d, Height: %d, Weight: %d, IQ: %d" % (age, height, weight, iq)


# A puzzle for the extra credit, type it in anyway.
print "Here is a puzzle."

# print "We are goingt to do the study drill for disecting 'what:'"

# what_divide = divide(iq, 2)
# what_multiply = multiply(weight, what_divide)
# what_subtract = subtract(height, what_multiply)
# what_add = add(age, what_subtract)
# what = what_add

# print "That becomes:", what, "Can you do it by hand?"

# what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

# print "That becomes:", what, "Can you do it by hand?"

print "Let's try this as a function:"

print "That becomes: %d Can you do it by hand?" % what()
