# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 16:50:05 2014

@author: ijoe
"""

def check_fermat(a,b,c,n):
    if n>2 and a**n+b**n == c**n:
        print "Holy smokes, Fermat was wrong!"
    else:
        print "NO, that doesn't work."
        
questiona = raw_input('What is the vale of a?\n')
questionb = raw_input('What is the value of b?\n')
questionc = raw_input('What is the value of c?\n')
questionn = raw_input('What is the value of n?\n')
a = int(questiona)
b = int(questionb)
c = int(questionc)
n = int(questionn)

check_fermat(a,b,c,n)