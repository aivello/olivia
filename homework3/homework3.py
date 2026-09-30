# --- Print Functions ---

def say_goodbye(name):
    # Says goodbye
    print ("Goodbye", name)

name = "Liv"
print(say_goodbye(name))

def circle(r):
    # tells you the area of a circle
    area = r *r * 3.14
    print(area)
r=8
print(circle(r))

# --- Return Functions ---

def subtract(a, b):
    # subtracts one number from another
    return a - b

def multiply(a, b):
    # multiplies two numbers
    return a * b

def divide(a, b):
    # divides one number from another
    return a / b

a = 10
b = 2

print(subtract(a, b))
print(multiply(a, b))
print(divide(a, b))

# --- Conditionals ---
def outfit(temp):
    # gives you the temperature of the day so you can decide what to wear
    return min(temp), max(temp) 

temp = (65, 68, 70, 73, 85, 90)
print(outfit(temp))

def is_weekend(day):
    # determines if it is the weekend or not
    if 6 <= day >= 7:
        return "True"
    else:
        return "False"

day = 7
print(is_weekend(day))

def fuel_efficiency(miles, gallons):
    # determines fuel efficiency in miles per gallon
    return miles/gallons

miles = 10
gallons = 2
print(fuel_efficiency(miles, gallons))

def encryption(integer):
    n = len(str(integer))
    digit = integer % 10
    integer = integer - digit
    integer = integer // 10
    integer = integer + digit * (10 ** (n-1))
    return integer

integer = 12345678
print(encryption(integer))

# --- Loops ---

def power(x, y):
    # raises x to the power of y
    value = x
    for i in range(1, y):
        value = value * x
    return value 

x = 2
y = 3
print(power(x, y))

def min(numbers):
    # tests which number in a list is the minimum
    test_min = numbers[0]
    for  num in numbers:
        if num < test_min:
            test_min = num
    return test_min

def max(numbers):
    # tests which number in a list is the maximum
    test_max = numbers[0]
    for num in numbers:
        if num > test_max:
            test_max = num
    return test_max



numbers = [5, 10, 15, 25, 30]
print(min(numbers))
print(max(numbers))

def sum(values):
    # takes the sum of the digits of integers
    value_sum = 0
    for digit in str(values) :
        value_sum += int(digit)
    return value_sum

values = 1234
print(sum(values))

# --- code from "Check if it's the weekend" function ---
day = 6 # the sixth day of the week
print(is_weekend(day)) # if the day is a weekend, it will print true. If not, it will print false.







    


