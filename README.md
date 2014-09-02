randomness
==========

bunch of little programs to do small things

1. donutcount  
-------------  
made with Python 3.3, tkinter

background:
Let's say you want to arrange a party and you want to buy donut holes. Of course, you want to save money so you need to calculate the right combination of large, medium, and small boxes that will cost you the least amount of money. And also, you don't like math very much. Well, that's okay because now you have this program I made!   

This program calculates the best combo of box sizes (large, med, small) a certain number of donuts to get the best price.  
It asks for the number of people you need to feed, as well as how many donuts you think each person will eat. Based on the total number of donuts, your answer will be given.  

adapted from here: http://cscircles.cemc.uwaterloo.ca/6d-design/  
thanks cscircles! :D

some notes to myself:  
root.bind('< Return >',donutCount) alone doesn't work, but getting Return to work happens if I first make a new function (i.e. def onclick():), make event="None", and execute donutCount() under onclick(). 
 
