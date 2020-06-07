# -*- coding: utf-8 -*-
"""
Created on Thu Mar 12 15:30:02 2020

@author: Manjeema
"""
"""
def his(pat,no):
    print(pat*no)

his('#',2)
his('@',4)
his('*',3)
his('&',2)
his('%',5)
 """           
def histogram(items,pat):
    for n in items:
        times = n
        print(pat*times)

items=[int(x) for x in input("Enter list: ").split()]
pat=input("Enter pattern: ")
histogram(items,pat)