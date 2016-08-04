#!/usr/bin/python

from sys import argv
from os.path import exists

script, arg1, arg2 = argv

def copy_a_file(old_file, new_file):
    infile = open(old_file, 'r')
    outfile = open(new_file, 'w')
    line = infile.readline()
    while line:
        outfile.seek(0, 2)
        outfile.writelines(line)
        line = infile.readline()
    infile.close()
    outfile.close()

copy_a_file(arg1, arg2)

# script, from_file, to_file = argv

# print "Copying from %s to %s" % (from_file, to_file)

# we could do these two on one line too, how? 
# in_file = open(from_file)
# indata = in_file.read()
# indata = open(from_file).read()

# print "The input file is %d bytes long" % len(indata)

# print "Does the output file exist? %r" % exists(to_file)
# print "Ready, hit RETURN to continue, CTRL-C to abort."
# raw_input()

# out_file = open(to_file, 'w')
# out_file.write(indata)

# print "Alrgiht, all done." 

