# -*- coding: utf-8 -*-
"""
Created on Fri Feb 28 18:04:27 2014

@author: ijoe
"""
import re

ignoringwords = ['a','an','the','to','that','who','i','we','my','this','our','of','is','in','how','who','what','when','where','why','from','for','and','so','are']

f = open("testolintext.txt","r")
full_text = f.read()

def get_word_counts_list(wordlist):
    l = []
    for i in range(len(wordlist)):
        thing = [wordlist[i],full_text.count(wordlist[i])]
        l.append(thing)
    return l
    
def get_word_counts_dict(wordlist,text):
    a = []
    for i in range(len(wordlist)):
        numword = text.count(wordlist[i])
        a.append(numword)
        d = dict(zip(wordlist,a))
    return d
    
def get_list_of_words(text):
    textlist = re.findall("[\w'\-]+",text)
    return textlist

def turn_text_to_lowercase(text):
    return text.lower()
    
def eliminate_unneeded_words(text):
    a = []
    listofwords = get_list_of_words(text)
    for i in range(len(listofwords)):
        if listofwords[i] not in ignoringwords:
            x = [listofwords[i]]
            a.append(x)
        else:
            