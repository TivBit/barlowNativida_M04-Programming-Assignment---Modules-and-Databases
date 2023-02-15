# -*- coding: utf-8 -*-
"""
Created on %(Date: 12 Feb 2023)s

@author: %(Tiv Barlow)s
Python Version 3.11.1
SDEV 220 Spring 2023
Assignment: M04 Programming Assignment - Modules and Databases
Chapter 16 Task: 16.8
"""

from flask import Flask
application = Flask(__name__)


class Book(): 
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
        
    def __str__(self):
        return f"{self.title} was written by {self.author} in {self.year}"
    

books = [
    Book("The Weirdstone of Brisingamen", "Alan Garner", 1960),
    Book("Perdido Street Station", "China Miéville", 2000),
    Book("Thud!", "Terry Pratchett", 2005),
    Book("The Spellman Files", "Lisa Lutz", 2007),
    Book("Small Gods", "Terry Pratchett", 1992)
    ]

    
    


######################## JSON

import json


with open("books2.json") as fromFile:
    data = []
    for line in fromFile:
        data.append(json.loads(line.strip()))
        
@application.route("/books")
def bookbag():
    with open("books2.json") as fromFile:
        for line in fromFile:
            yield line.strip()
            
@application.route("/books/<year>")
def bookbag_year(year):
    with open("books2.json") as fromFile:
        
            def year(title, author, year):
                
            #Iterate through lines
              for i, line in enumerate(fromFile):
            
                #Choose specific book year to print.
                if year == year:
                    print(line)
                                    
                else:
                    return f"There are no books printed in the year {year}."
                   
            print(line)
            yield "hello world"
            
            
        