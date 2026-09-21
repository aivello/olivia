name = "Olivia"

# print("Hello," name)

def say_hello(name):
    print("Hello,", name)
say_hello(name="Olivia")

def add(a,b):
    return(a+b)
print(add(2,4))

'''
if: checks if a condition is true

elif: checked if first if was false
(can have multiple elif statements)

else: catches everything else if none of the other statements are deemed true
'''

def check_num(num):
    if num>0:
        return "Positive"
    elif num<0:
        return "Negative"
    else:
        return "Zero"

print(check_num(42))

print(True and False)

'''
Conditional Statements

and: both conditions must be True

or: one condition must be True
'''

def can_vote(age, is_citizen):
    if age >= 18 and is_citizen:
        print("You can vote!")
    else:
        print("You cannot vote")

can_vote(19, True)

def is_weekend(day):
    if day=="Saturday" or day=="Sunday":
        return "It is the weekend!"
    else:
        return "It is not the weekend!"

print (is_weekend("Monday"))

'''
While Loop Syntax

while a condition is True, do something
needs to always make sure the condition eventually becomes false
'''

for i in range(10):
    print(i)

fruit_basket = ["Lychee", "mango", "nectarines"]

for fruit in fruit_basket:
    print(fruit)

def countdown(start): 
    while start>0:
        print("T-",start)
        start -= 1
    print("Lift off")

countdown(10)

    


