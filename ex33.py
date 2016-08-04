#!/usr/bin/python

# instantiate 'i' with a 0 value
i = 0
# create an empty list called numbers
numbers = []
start = int(raw_input("What should we count from? > "))
maxcount = int(raw_input("How high should we count? > "))
increment = int(raw_input("How many numbers should we skip inbetween? > "))


def list_to_max(num_list, base, maxcount, inc_by):
    if num_list.__len__() == 0:
        for j in range(start, maxcount, inc_by):
            print "At the top count is %d" % j
            num_list.append(j)
            j += inc_by
            print "Numbers now:", num_list
            print "At the bottom count is %d" % j
        return num_list
    else:
        print "List provided was not empty"
        exit()

numbers = list_to_max(numbers, start, maxcount, increment)

# print a headed
print "The numbers:"
# create a for loop that iterates through the contents of (list)numbers
for num in numbers:
    # print out the current value stored in num which is derived from
    # (list)numbers
    print num
