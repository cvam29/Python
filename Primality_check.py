# -*- coding: utf-8 -*-
"""
Created on Wed Feb 17 14:42:20 2021

@author: home
"""

#Program to check if number is Prime
num=int(input('Enter the number :'))
if num>1:
    for i in range(2,num):
        if num%i==0:
            print('Number is not  prime ')
            break
    else:
            print(num,'is prime')
