# -*- coding: utf-8 -*-
"""
Created on Fri Feb 28 18:04:27 2014

@author: ijoe
"""

#Things to import
import re
import os
from collections import Counter

#Words we want to ignore when analyzing text
ignoringwords = ['a','an','then','the','it','if','you',"you're",'your','was','to','as','that','who','i','we','my','this','our','of','with','is','in','how','who','what','when','where','why','from','for','and','so','are','had','has','have']

#open and read text
f = open("testolintext.txt","r")
full_text = f.read()
t = open("textsample1.txt","r")
textsample1 = t.read()

#functions
def get_top_n_words_dict_to_list(text,n):
    '''This function takes an input of text and the top number of words we want 
    to look at and outputs a list of all words in the text and how many 
    times it appears. Inside this function the list of words turns into a dictionary
    and then back to a list.'''
    ntext = turn_text_to_lowercase(text)
    nlist = eliminate_unneeded_words(text)
    a = []
    for i in range(len(nlist)):
        numword = ntext.count(nlist[i])
        a.append(numword)
        d = dict(zip(nlist,a))
        c = Counter(d)
    return c.most_common(n)
        
            

#Unit test for get_word_counts_dict
def get_top_n_words_dict_to_list_unit_test():
    a  = "Mary had a little lamb, little lamb, little lamb. Mary had a little lamb and it was white as snow."
    print "input: ",a
    print "expected output:[('lamb',4),('little',4),('mary',2)]"#not in alphabetical order but in actual result, will be
    print "actual output:",get_top_n_words_dict_to_list(a,3)
    
    b = "If you're happy and you know it clap your hands. If you're happy and you know it clap your hands. If you're happy and you know it and you really want to show it if you're happy and you know it clap your hands."
    print "\ninput: ",b
    print "expected output: [('know',4),('happy',4),('hands',3)]"
    print "actual output",get_top_n_words_dict_to_list(b,3)


def get_list_of_words(text):
    '''This function takes an input of plain text and returns the text into a
    list of words.'''
    textlist = re.findall("[\w'\-]+",text)
    return textlist

#Unit test for get_list_of_words
def get_list_of_words_unit_test():
     a  = "Mary had a little lamb, little lamb, little lamb. Mary had a little lamb and it was white as snow."
     print "input: ",a
     print "expected output: ['Mary', 'had', 'a', 'little', 'lamb', 'little', 'lamb', 'little', 'lamb', 'Mary', 'had', 'a', 'little', 'lamb', 'and', 'it', 'was', 'white', 'as', 'snow']"
     print "actual output:",get_list_of_words(a)
     
     b = "If you're happy and you know it clap your hands. If you're happy and you know it clap your hands. If you're happy and you know it and you really want to show it if you're happy and you know it clap your hands."
     print "\ninput: ",b
     print "expected output: ",str(['If', "you're", 'happy', 'and', 'you', 'know', 'it', 'clap', 'your', 'hands', 'If', "you're", 'happy', 'and', 'you', 'know', 'it', 'clap', 'your', 'hands', 'If', "you're", 'happy', 'and', 'you', 'know', 'it', 'and', 'you', 'really', 'want', 'to', 'show', 'it', 'if', "you're", 'happy', 'and', 'you', 'know', 'it', 'clap', 'your', 'hands'])
     print "actual output:",get_list_of_words(b)


def turn_text_to_lowercase(text):
    '''This function takes plain text as input and returns the same text all in lowercase.
    We're using this function so that when we look for words, same words of different
    capitalization are not set as different words.'''
    return text.lower()

#Unit test for turn_text_to_lowercase
def turn_text_to_lowercase_unit_test():
    print "input :Olin College is in NeeDHAM"
    print "expected output: olin college is in needham"
    print "actual output:",turn_text_to_lowercase("Olin College is in NeeDHAM")
    
    print "\ninput :This HOMEWORK will END in ten minutes."
    print "expected output: this homework will end in ten minutes"
    print "actual output:",turn_text_to_lowercase("This HOMEWORK will END in ten minutes.")
    
def eliminate_unneeded_words(text):
    '''This function takes an input of plain text and returns the text with the words
    in ignoringwords list removed.'''
    newtext = turn_text_to_lowercase(text)
    listofwords = get_list_of_words(newtext)
    newlist = [i for i in listofwords if i not in ignoringwords]
    return newlist
    
#Unit test for eliminate_unneeded_words
def eliminate_unneeded_words_unit_test():
    a  = "Mary had a little lamb, little lamb, little lamb. Mary had a little lamb and it was white as snow."
    print "input: ",a
    print "expected output: ['mary','little','lamb','little','lamb','little','lamb','mary','little','lamb','white','snow']"
    print "actual output: ",eliminate_unneeded_words(a)

    b = "If you're happy and you know it clap your hands. If you're happy and you know it clap your hands. If you're happy and you know it and you really want to show it if you're happy and you know it clap your hands."
    print "\ninput: ",b
    print "expected output: ['happy', 'know', 'clap', 'hands', 'happy', 'know', 'clap', 'hands', 'happy', 'know', 'really', 'want', 'show', 'happy', 'know', 'clap', 'hands']"
    print "acutal output:",eliminate_unneeded_words(b)

def get_list_of_txt_files_in_dir(path):
    '''This function takes a path or a directory and outputs a list of all 
    .txt files in the directory.'''
    listoftxt = []
    for f in os.listdir(path):
        if f.endswith(".txt"):
            listoftxt.append(f)
    return listoftxt

def get_most_freq_words(path,n):
    '''This function takes a path or a directory and the top number of words we want
    to look at and returns the n number of most frequently used words in all text files
    inside the directory.'''
    a = get_list_of_txt_files_in_dir(path)
    y = ''
    for i in range(len(a)):
        x = open(a[i],'r')
        y += x.read()
        z = get_top_n_words_dict_to_list(y,n)
    return z         
          