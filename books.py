# -*- coding: utf-8 -*-
"""
Created on %(Date: 12 Feb 2023)s

@author: %(Tiv Barlow)s
Python Version 3.11.1
SDEV 220 Spring 2023
Assignment: M04 Programming Assignment - Modules and Databases
Chapter 16 Task: 16.8
"""

from flask import flask
application = flask.Flask(__name__)


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

"""
with open("books2.json", "w") as toFile:
    for b in books:
        toFile.write(json.dumps({"author": b.author, "title": b.title, "year": b.year}) + "\n")
"""

with open("books2.json") as fromFile:
    data = []
    for line in fromFile:
        data.append(json.loads(line.strip()))
        
@application.route("/books")
def bookbag():
    with open("books2.json") as fromFile:
        for line in fromFile:
            yield json.loads(line.strip())        
            
        