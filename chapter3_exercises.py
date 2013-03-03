# Exercises for chapter 3: Problems 3.1, 3.2, 3.3, and 3.4 in Think Python

# Michael Ko

#3.1

#repeat_lyrics() - If function call appears before the definitions, error of function not defined. 
#NameError: name 'repeat_lyrics' is not defined

def print_lyrics():
    print "I'm a lumberjack, and I'm okay."
    print "I sleep all night and I work all day."

def repeat_lyrics():
    print_lyrics()
    print_lyrics()

repeat_lyrics() 

#3.2
def print_lyrics():
    print "I'm a lumberjack, and I'm okay."
    print "I sleep all night and I work all day."

def repeat_lyrics():
    print_lyrics()
    print_lyrics()

repeat_lyrics() 
print_lyrics()
# Program results in print_lyrics() function being called a total of 3 times. 

#3.3
#3.3 problem 1 - Prints "spam" twice.
def right_justify(a, b):
	print (' '*(b-len(a))+a)
endcol = 70	
name = 'allen'
right_justify(name, endcol)

#3.4
def do_twice(f):
    f()
    f()

def print_spam():
    print "spam"

do_twice(print_spam)
#3.3 problem 2
def do_four(f):
    do_twice(f)
    do_twice(f)

do_four(print_spam)

#3.3 problem 3
def print_twice(n):
    print n
    print n

n = "string print twice"

print_twice(n)

#3.4 problem 4
do_twice(print_spam)




