# -*- coding: utf-8 -*-
"""
Created on Wed Feb 17 15:09:37 2021

@author: home
"""

string=input('Enter the string: ')
temp=string.lower()
reverse_string=string[::-1].lower()
if temp==reverse_string:
    print('The string is palindrome')
else:
    print('Not a palindrome')