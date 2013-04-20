# This is where Exercise 5.4 goes
# Name: Brian Yee

def is_triangle(s1,s2,s3):
    if s1 > (s2 + s3):
        print "No"
    elif s2 > (s1 + s3):
        print "No"
    elif s3 > (s2 + s1):
        print "No"
    else:
        print "Yes"

def get_sides():
    s1 = raw_input("Input side length 1:")
    s2 = raw_input("Input side length 2:")
    s3 = raw_input("Input side length 3:")
    is_triangle(float(s1),float(s2),float(s3))

get_sides()