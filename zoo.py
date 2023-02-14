# -*- coding: utf-8 -*-
"""
Created on %(Date: 12 Feb 2023)s

@author: %(Tiv Barlow)s
Python Version 3.11.1
SDEV 220 Spring 2023
Assignment: M04 Programming Assignment - Modules and Databases
Chapter 11 Tasks: 11.1 & 11.2
"""

# 11.1--Create a file called zoo.py. In it, define a function called hours() 
# that prints the string 'Open 9-5 daily'. Then, use the interactive 
# interpreter to import the zoo module and call its hours() function.

import zoo

def hours():
    print('Open 9-5 daily')
    
hours()

####################################################################
####################################################################

# 11.2-- In the interactive interpreter, import the zoo module as menagerie 
# and call its hours() function.

import zoo as menagerie
menagerie.hours()


####################################################################
print()
####################################################################

