# -*- coding: utf-8 -*-
"""
Created on %(Date: 12 Feb 2023)s

@author: %(Tiv Barlow)s
Python Version 3.11.1
SDEV 220 Spring 2023
Assignment: M04 Programming Assignment - Modules and Databases-Ch 16
Chapter 16 Task: 16.8
"""

from books import Book

books = [
    Book("The Weirdstone of Brisingamen", "Alan Garner", 1960),
    Book("Perdido Street Station", "China Miéville", 2000),
    Book("Thud!", "Terry Pratchett", 2005),
    Book("The Spellman Files", "Lisa Lutz", 2007),
    Book("Small Gods", "Terry Pratchett", 1992)
    ]



############## binary file

import pickle

with open("books.csv", "wb") as toFile:
    pickle.dump(books, toFile)
    

with open("books.csv", "rb") as fromFile:
    stuff = pickle.load(fromFile)
    print(stuff[3])




############## SQLite

import sqlite3 as sql

db = sql.connect("books.db")

createQuery = "CREATE TABLE IF NOT EXISTS People(Name TEXT, Age INTEGER, Town TEXT);"

db.execute(createQuery)

for b in books:
    insertQuery = "INSERT INTO Books(Author, Title, Year) VALUES(\"" + p.author + "\", " + p.title + ", \"" + str(p.year) + "\");"
    cursor = db.execute(insertQuery)
    if cursor.rowcount >= 0:
        print("added the data")
    else:
        print("there was an error")
        
    
    
selectQuery = "SELECT author, title, year FROM Books WHERE title >= ___;" #<--ASK CHRIS!


cursor = db.execute(selectQuery)
for row in cursor:
    print(row[0])
    
db.close()