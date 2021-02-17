# -*- coding: utf-8 -*-
"""
Created on Wed Feb 17 15:03:41 2021

@author: Shivam
"""

#Program to Reverse a number
num=int(input('Enter the number: '))
test_num=0
temp=num
while num>0:
    remainder=num%10
    test_num=(test_num*10)+remainder
    num=num//10
print('the reversed number is :{}'.format(test_num))
if temp==test_num:
    print('The number is palindrome')
else:
    print('The number is not palindrome')
