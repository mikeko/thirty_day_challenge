# Exercises for chapter 2: Problems 2.1, 2.2, 2.3, and 2.4 in Think Python

# Michael Ko

#2.1
zipcode = 2492
print "%05d" % (zipcode)

#2.2
print "5"
x = 5
x = x + 1
print x

#2.3
width = 17
height = 12.0
delimiter = "."
#2.3 problem 1
w1 = width/2
print 'width/2 = {}'.format(w1)
print type(w1) 
#2.3 problem 2
w2 = width/2.0
print 'width/2 = {}'.format(w2)
print type(w2) 
#2.3 problem 3
h1 = height/3
print 'height/3 = {}'.format(h1)
print type(h1) 
#2.3 problem 4
p1 = 1 + 2 * 5
print '1 + 2 * 5 = {}'.format(p1)
print type(p1) 
#2.3 problem 5
p2 = delimiter * 5
print 'delimiter * 5 = {}' .format(p2)
print type(p2) 

#2.4 problem 1
import math
r = 5
v = (((4.0/3.0)*math.pi)*r**3.0)
print 'Volume of a sphere with a radius of 5 is {}'.format(v)

#2.4 problem 2
price = 24.95
disc = 1 -.4
ship1 = 3
ship2 = .75
units = 60
booktotal = ((price*disc)*units)
shiptotal = (ship1+((units-1)*ship2))
total_cost = booktotal+shiptotal
print 'Total wholesale cost is ${}'.format(total_cost)

#2.4 problem 3
starthour = 6
startmin = 52
easymin = 8
easysec = 15
tempomin = 7
temposec = 12
easypace = 2
tempopace =3

easytime_sec = (((easymin*60)+easysec)*easypace)
tempotime_sec = (((tempomin*60)+temposec)*tempopace)
runtime_sec = easytime_sec+tempotime_sec

currenttime_sec = ((starthour*3600) + (startmin*60))
endtime_sec = currenttime_sec + runtime_sec

endhour = endtime_sec/3600
endmin = (endtime_sec % 3600)/60

print 'Back for breakfast at {}:{}' .format(endhour, endmin)




