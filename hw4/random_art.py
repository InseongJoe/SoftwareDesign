# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 11:34:57 2014

@author: pruvolo
"""

# you do not have to use these particular modules, but they may help
from math import *
from random import *
import Image

def build_random_function(min_depth, max_depth):
    # your doc string goes here
    '''This function takes in the minimum depth and the maximum depth and outputs 
    a random function of random depth.'''
    # your code goes here
    i = randint(min_depth,max_depth)
    if i == 1:
        return choice([["x"],["y"]])
    else:
        return choice([["p1",build_random_function(i-1,i-1),build_random_function(i-1,i-1)],["p2",build_random_function(i-1,i-1),build_random_function(i-1,i-1)],["prod",build_random_function(i-1,i-1),build_random_function(i-1,i-1)],["cos_pi",build_random_function(i-1,i-1)],["sin_pi",build_random_function(i-1,i-1)],["avg",build_random_function(i-1,i-1),build_random_function(i-1,i-1)],["sqr",build_random_function(i-1,i-1)]])
        
def evaluate_random_function(f, x, y):
    # your doc string goes here
    '''This function takes in the random function created and the x and y values 
    and outputs the evaluation of the random function using the x and y.'''
    # your code goes here
    if f[0] == "x":
        return x
    elif f[0] == "y":
        return y
    else:
        if f[0] == "sin_pi":
            return sin(pi* evaluate_random_function(f[1] ,x,y ))
        elif f[0] == "prod":
            return evaluate_random_function(f[1],x,y)*evaluate_random_function(f[2],x,y)
        elif f[0] == "cos_pi":
            return cos(pi*evaluate_random_function(f[1],x,y))
        elif f[0] == "avg":
            return (evaluate_random_function(f[1],x,y)+evaluate_random_function(f[2],x,y))/2.0
        elif f[0] == "sqr":
            return evaluate_random_function(f[1],x,y)**2
        elif f[0] == "p1":
            return evaluate_random_function(f[1],x,y)
        elif f[0] == "p2":
            return evaluate_random_function(f[2],x,y)
        

def remap_interval(val, input_interval_start, input_interval_end, output_interval_start, output_interval_end):
    """ Maps the input value that is in the interval [input_interval_start, input_interval_end]
        to the output interval [output_interval_start, output_interval_end].  The mapping
        is an affine one (i.e. output = input*c + b)."""
    # your code goes here
    return (val-input_interval_start)/float((input_interval_end - input_interval_start))*(output_interval_end - output_interval_start) + output_interval_start


#make image here

#make random functions for red green and blue
r_func = build_random_function(2,3)
g_func = build_random_function(3,5)
b_func = build_random_function(2,6)

#create image and pixels
im = Image.new("RGB",(350,350))
pix = im.load()
#set x and y intervals to (-1,1) and then each color to (0,255)
for x in range(0,350):
    xnew = remap_interval(x,0,350,-1,1)
    for y in range(0,350):
        ynew = remap_interval(y,0,350,-1,1)
        r = evaluate_random_function(r_func,xnew,ynew)
        g = evaluate_random_function(g_func,xnew,ynew)
        b = evaluate_random_function(b_func,xnew,ynew)
        rc = remap_interval(r,-1,1,0,255)
        gc = remap_interval(g,-1,1,0,255)
        bc = remap_interval(b,-1,1,0,255)
        pix[x,y] = (int(rc),int(gc),int(bc))
#save image
im.save("img3.JPEG")

    