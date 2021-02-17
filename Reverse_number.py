# -*- coding: utf-8 -*-
"""
Created on Wed Feb 17 14:52:16 2021

@author: home
"""

#Program to Reverse a number
num=int(input('Enter the number: '))
test_num=0
while num>0:
    remainder=num%10
    test_num=(test_num*10)+remainder
    num=num//10
print('the reversed number is :{}'.format(test_num))