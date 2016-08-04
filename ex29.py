#!/usr/bin/python

people = int(raw_input("How many people? > "))
cats = int(raw_input("How many cats? > "))
dogs = int(raw_input("How many dogs? > "))


if people < cats:
    print "Too many cats! The world is doomed!"

if people > cats:
    print "Not many cats! The world is saved!"

if people < dogs:
    print "The world is drooled on!"

if people > dogs:
    print "The world is dry!"

if people / 5 >= dogs:
    answer = raw_input("There are fewer than one dog per five people, do you want to add some dogs? > ")
    print "Answer: %s" % answer
    print "Answer.lower(): %s" % answer.lower()
    if answer.lower() == "yes":
        dogs += people / 5
        print "Now there are %d dogs, yay!" % dogs

if people >= dogs:
    print "People are greater than or equal to dogs."

if people <= dogs:
    print "People are less than or equal to dogs."


if people == dogs:
    print "People are dogs."
