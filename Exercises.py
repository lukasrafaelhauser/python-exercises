#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 26 14:35:40 2018

@author: l-r-h
"""

#%%

def linear(lst, number):
    for i in range(len(lst)):
        if number == lst[i]:
            return i
    
    return None

#%%
    
