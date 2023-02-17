# -*- coding: utf-8 -*-
"""
Created on %(Date: 12 Feb 2023)s

@author: %(Tiv Barlow)s
Python Version 3.11.1
SDEV 220 Spring 2023
Assignment: M04 Programming Assignment - Modules and Databases-Ch 16
Chapter 16 Task: 16.8
"""
import sqlite3 as sql


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

book_info = Book(year, author, year)
print(Book)

############## SQLite
db = sql.connect("books.db")
curs = db.cursor()

createQuery = "CREATE TABLE IF NOT EXISTS People(Title TEXT, Author TEXT, Year INTEGER);"

db.execute(createQuery)

for b in books:
    insertQuery = "INSERT INTO Books(Title, Author, Year) VALUES(\"" + b.title + "\", " + b.author + ", \"" +str(b.year) + "\");"
    cursor = db.execute(insertQuery)
    if cursor.rowcount >= 0:
        print("added the data")
    else:
        print("there was an error")
        
        
selectQuery = "SELECT title, author, year FROM Books ORDER BY last_name ASC;"


cursor = db.execute(selectQuery)
for row in cursor:
    print(row[0])
    
db.close()


