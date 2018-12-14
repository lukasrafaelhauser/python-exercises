#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 11 21:50:42 2018

@author: l-r-h
"""
#%%

class Product:
    def __init__(self, name, quality):
        self.name = name
        self.quality = quality


def recalculate_quality(product):
    if product.name == "potato":
        product.quality = product.quality - 0.5
    elif product.name == "cheese":
        product.quality = product.quality - 2
    else:
        if product.quality < 5:
            product.quality -= 3

potato = Product("potato", 5)
cheese = Product("cheese", 3)
ham = Product("ham", 4)
tomato = Product("tomato", 0)
banana = Product("banana", -6)

#%%