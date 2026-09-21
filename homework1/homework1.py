# File: homework1.py

# ---Variables and Data Types---

a=10
print(a)
print(type(a))
# a is an integer

b=1.5
print(b)
print(type(b))
# b is a float, a number with a decimal point

c=3j
print(c)
print(type(c))
# c is a complex number, a number and a letter

d="Hello"
print(d)
print(type(d))
# d is a string

e=[1, 2, 3]
print(e)
print(type(e))
# e is a list 

f={"name": "Ellen", "favorite fruit": "strawberry"}
print(f)
print(type(f))
# f is a dict

g=(1, 2)
print(g)
print(type(g))
# g is a tuple

h=["apple", "banana", "strawberry",]
print(h)
print(type(h))
# h is a list

i=True
print(i)
print(type(i))
# i is a boolean

j=None
print(j)
print(type(j))
# j is a NoneType

k=[True, "blue", 12]
print(k)
print(type(k))
# k is a list

l=str(14)
print(l)
print(type(l))
# l is an string

m=1e4
print(m)
print(type(m))
# m is a float

'''
Questions
1) I found 9 data types
2) float, integer, string, list, complex number, boolean, NoneType, tuple, dict
3) m and b are bothe floats, l and d are both strings, k and h are both lists
4) The data type of l is a string and not an integer because str() converts the object into a string.
'''

s1={"a", "b", "c", "d", "e"}
print(s1)
print(type(s1))
# s1 is a set


# ---Booleans---
print(bool(10>0)) # True, 10 is greater than 0
print(bool(10==9)) # False, 10 does not equal 9
print(bool(10<=9)) # False, 10 is not less than or equal to 9
print(bool("abc")) # True, this is a string with an object inside
print(bool(123)) # True, this is an integer not equal to 0
print(bool(["apples", "cherry", "banana"])) # True, adding the bracket turns the words into a list that is not empty
print(bool(True)) # True, it says true so it is true
print(bool(False)) # False, it says false so it is false
print(bool(0)) # False, the integer being 0 makes it false
print(bool("")) # False, the string is empty which makes it false
print(bool(" ")) # True, the space turns it into a string so it is true
print(bool(())) # False, it is blank so it is false
print(bool([])) # False, it is blank so it is false
print(bool({})) # False, it is blank so it is false
print(bool(True and False)) # False, it is required that both sides of the expression are truthy in an 'and' statement
# for it to be true therefore it is false
print(bool(True and True)) # True, both sides of the expression are true
print(bool(False and False)) # False, both sides of the expression are false
print(bool(True or False)) # True, in an 'or' statement only half of the expression needs to be
# true for it to be true so this statement is true
print(bool(True or True)) # True, both sides of the expression are true
print(bool(False or False)) # False, both sides of the expression are false
print(bool(not(False))) # True, not false is true
print(bool(not(True))) # False, not true is false


'''
Questions
1) The expressions are true if they resemble true equations or non-blank strings. The 
expressions are false depending on how many sides of the 'and' or 'or' expressions are true or false
2) True or False being true surprised me because it didn't follow the pattern of the 'and' expressions
3) print(bool(1+1=2)) will return true because the equation is true.
4) print(bool(1+1=4)) will return false because the equation is false.
'''

# ---Operators---

# ---Arithmetic Operators---
print(10 + 5) # 15, performs addition
print (10 - 5) # 5, performs subtraction
print(2 * 4) # 8, performs multiplication
print(6 / 3) # 2.0, performs division
print(5 % 2) # 1, gives the percent a number is of another number
print(3 ** 2) # 9, performs exponentiation
print (15 // 2) # 7, performs division and rounds down to the nearest integer

# ---Comparison Operators---
print(5 == 2) # False, tells you if an equation is true or not
print(10 != 10) # False, tells you if an equation with a factorial is true or false
print(2 < 5) # True, tells you if a number is less than another number
print(12 > 5) # True, tells you if a number is greater than another number
print(5 <= 6) # True, tells you if a number is less than or equal to another number
print(1 >= 10) # False, tells you if a number is greater than or equal to another number

# ---Assignments Operators---
x=5

x += 5
print(x)

x -= 4
print(x)

x *= 3
print(x)

# ---Logical Operators---
'''
Questions
1) The operator "and" is used to combine multiple conditional statements.
An expression that would result in True would be print(bool(True and True)).
An expression that would result in False would be print(bool(True and False)).
2) the operator "or" is used to check if at least one side of the expression is correct.
An expression that would result in True would be print(bool(True or False)).
An expression that would result in False would be print(bool(False or False.))
3) The operator "not" reverses if an expression is true or false.
An expression that would result in True would be print(bool(not(False))).
An expression that would result in False would be print(bool(not(True))).

More Questions
1) / divides numbers normally, // divides numbers and rounds down to the nearest integer.
2) % gives the percent of a number is of another number, // is used for division.
3) you would use the arithmetic operator / to calculate the remainder of another number because using // would round
to an integer. For example, to find the remainder of 5/3, running the command print(5 // 3) would result in the number 1.
However, when you run print(5 / 3) instead, you are left with 1.66 ... , which tells you the remainder.
4) Assignment operators work by taking an already defined variable and doing different operations to it in order to change 
the value of that variable to something else (changes a variable from one number to another).

'''

# ---Strings---
my_string = "hello"
print(my_string) # prints hello
print(my_string[0]) # prints the first letter of the string
print(my_string[1]) # prints the second letter of the string
print(my_string[2]) # prints the third letter of the string
print(my_string[3]) # prints the fourth letter of the string
print(my_string[4]) # prints the fifth letter of the string
print(my_string[-1]) # prints the last letter of the string
print(my_string[1:3]) # prints the second and fourth letters of the string
print(my_string[0:5:2]) # prints every 2 letters in the range from letters 0-5
print(len(my_string)) # shows you how many letters a string is
s="goodbye"
print((my_string)+(s))
print((my_string)*(7))

'''
Questions
1) slicing in python allows you to print individual components of a string without having
to modify the string itself. The string was sliced in mutations 8 and 9.
'''

name = "Oski"
print("Hello, my name is", name) # prints as "Hello, my name is Oski"

name = "Oski"
print(f"Hello, my name is {name}") # prints as "Hello, my name is Oski"

'''
4) The difference between the two print statements is that the first one put two strings together,
whereas the second one is an f string which input the "Oski" string into the other string.
'''

# ---Terminal Commands---

# cd
# changes directories, navigates between folders
# Exampe: cd homework1

# ls
# lists the directories in your current working directory
# Example: ls

# ls -a
# shows all files in a directory including hidden files starting with a dot
# Example: ls -a

# mkdir
# makes a new directory
# Example: mkdir homework1

# cat
# displays all the contents of a text file onto your screen
# example: cat homework1.txt

# pwd
# prints your entire working directory
# Example: pwd

# cd ..
# lets you change to the "parent directory" which is the directory above the one you're in
# Example: cd ..

# cd . 
# doesn't change your directory at all because a single dot represents your current directory
# Example: cd .

# cd ~
# moves you directly to your home directory
# Example: cd ~

# cp
# used to copy directories from one location to another
# Example: cp homework1.txt homework2.txt (would duplicate to another file in the same directory)

# mv
# is used to move or rename directories
# Example: mv homework1 /home/oliviawolff/homework 

# rm
# permanently deletes directories
# example: rm homework2

# clear
# clears what is in your terminal
# Example: clear

# grep
# picks out words of your choosing within a file
# Example: grep "Example:" homework1.txt

'''
Questions
1) 
locate: locates the path of a file. For example, locate homework1.txt would show you the path to get to that file
echo: repeats text in the terminal. For example, echo "Hello World" would print the words into the terminal.
cal: displays the calender of the current month. For example, cal would display the month of September.
2) ls lists all the directories in your current working directory, while ls -a does the same thing but also shows 
hidden files. 
3) a hidden file is a file that begins with a period.
4) cd -L makes the shell follow symbolic links (established in the ln command) instead
of following the normal directory pathway
pwd -L does the same thing and shows your entire working directory keeping the symbolic links.
ls -t sorts the files by time, so it will show the newest files first and the oldest files last.
'''




