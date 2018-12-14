# -*- coding: utf-8 -*-

#%%

from Stock_quality import recalculate_quality, potato, cheese, ham, tomato, banana


def test_stock_quality_potato():
    recalculate_quality(potato)
    assert potato.quality == 4.5

def test_stock_quality_cheese():
    recalculate_quality(cheese)
    assert cheese.quality == 1
    
def test_stock_quality_ham():    
    recalculate_quality(ham)
    assert ham.quality == 1
    
def test_stock_quality_tomato_twice():
    recalculate_quality(tomato)
    recalculate_quality(tomato)
    assert tomato.quality == -6

def test_stock_quality_banana():
    recalculate_quality(banana)
    assert banana.quality == -3
        