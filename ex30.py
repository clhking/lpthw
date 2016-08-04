#!/usr/bin/python
import sys, os, numpy as np

people = np.random.random_integers(1000)
cars = np.random.random_integers(1000)
buses = np.random.random_integers(1000)

print "There are %d people, %d cars, and %d busses." % (people, cars, buses)

if cars > people:
    print "We should take the cars."
elif cars < people:
    print "We should not take the cars."
else: 
    print "We can't decide."

if buses > cars:
    print "That's too many buses."
elif buses < cars:
    print "Maybe we could take the buses."
else: 
    print "We still can't decide."

if people > buses:
    print "Alright, le's just take the buses."
else:
    print "Fine, let's stay home then."
