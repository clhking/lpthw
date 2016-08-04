#!/usr/bin/python

# Import the argv function from the sys module
from sys import argv

# pull in the command line arguments and assign to 'script' and 'input_file'
script, input_file = argv

# define a function to print an entire file.
def print_all(f):
    # pass print the entire contents of the file
    print f.read()

# define a function to rewind to the beginning of the file
def rewind(f):
    # seek to 0,0 which is 0 offset and 0 position (beginning)
    f.seek(0)

# create a function called print_a_line, pass it the line count and an input_file
def print_a_line(line_count, f):
    # pass print the line number index and the current line
    print line_count, f.readline()

# Create a file object and give it the filehandle of 'input_file'
current_file = open(input_file)

print "First let's print the whole file:\n"

# Run print_all and pass it the file object for 'input_file'
print_all(current_file)

print "Now let's rewind, kind of like a tape."

# Run rewind and pass it the file object for 'input_file'
rewind(current_file)

print "Let's print three lines:"

current_line = 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)
