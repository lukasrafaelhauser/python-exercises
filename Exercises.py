#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 26 14:35:40 2018

@author: l-r-h
"""

#%%

def linear(lst, element):
    for i in range(len(lst)):
        if element == lst[i]:
            return i
    
    return None

#%%

def hello():
    name = input("What's your name?")
    print("hello" + name)
        
#%%
    