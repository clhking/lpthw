#!/usr/bin/python

# import the argv function from the sys module
from sys import argv

# setup two variables and set them to the two strings expected from input 
# arguments to python. 
script, filename = argv

# instantiate a variable and set it to the filehandle of the file indicated
# in the 'filename' variable
txt = open(filename)

# print out a line confirming the filename to be read
print "Here's your file %r:" % filename

# print the file contents using the read function of the text variable.
print txt.read()

txt.close()

# print out a request to provide the filename again
print "Type the filename again:"
# set a variable type string called file_again by getting input from 
# the command line using raw_input
file_again = raw_input("> ")

# set a variable to hold the file handle of the filename specified
# in 'file_again'
txt_again = open(file_again)

# print the contents of the file given in 'txt_again' using the read function
print txt_again.read()

print "The filehandle for %s, is %r." % (txt_again, txt_again.fileno())

txt_again.close()
