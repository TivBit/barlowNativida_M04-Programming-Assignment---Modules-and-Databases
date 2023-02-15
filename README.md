# barlowNativida_M04-Programming-Assignment---Modules-and-Databases
This is the SDEV 220 Spring Module 4 Programming Assignment about Modules and Databases

This repository is the Module 04 Programming assignment for SDEV 220 Spring, by T.Barlow | Professor C. Francis.  The zoo.py for chapter 11's task is to create a program that will display the daily hours of the zoo.  The rest of the files are for the Books Assignment.  Please see the bug report below.

Bug Report:
The Zoo program seems to be working with no issues.  HOWEVER, the Books project seems to continue return an error in the console saying that the flask module can't be found.  I installed flask in the Windows Powershell Console and it said that the install was successful.  I have tried to run in the live and virtual environment, with no success.  I will be meeting with my instructor tomorrow to see if I can find my error.  Feedback is appreciated. Programming Student: T.Barlow | Professor: C. Francis

Update and Addendum to Bug Report:

Met with instructor and was able to figure out where the disconnect was, I had to reboot kernel after updating properties in Spyder to run on the version of Python that I was using, 3.11.  Spyder was running on verstion 3.8.  After I was able to get the program to run, I added a sub-class, (year) to be able to filter the books.  The entire book list did populate in the Windows Powershell Command Window.  I then updated the program to be able to only print one line from the list based on the year that was selected by the user in the browser window.  I was able to get one line to print, but it did not match the year selected.
