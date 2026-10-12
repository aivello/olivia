# --- Lists ---
# List Operations
fav_foods = ["Sushi", "Poke", "Cookies", "Bulgogi", "Noodles"]
print(fav_foods[1])
print(fav_foods[-4])
fav_foods.append("Watermelon")
print(fav_foods)
fav_foods.insert(0, "Hot Dog")
print(fav_foods)
fav_foods.remove("Cookies")
print(fav_foods)
print(len(fav_foods))

for food in range(len(fav_foods)):
    print(fav_foods[food].upper())

fav_foods_2 = fav_foods[0], fav_foods[-1]
print(fav_foods_2)

for food in fav_foods:
    if food == "potato":
        print("A potato!")
    else:
        print("No potato!")

# Slicing and Striding
numbers = list(range(0, 21))
print(numbers)

def get_first_15(list1):
    return list1[:15]

def get_every_5th(fifteen):
    return (fifteen[::5])

def reverse_and_stride(every_five):
    return (every_five[::-3])

print(reverse_and_stride(get_every_5th(get_first_15(numbers))))

# ---Nested Lists---
# Nested List Operations
numbers = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(numbers[2])
print(numbers[1][1])
numbers.append([10, 11, 12])
print(numbers)

def sum_nested(numbers):
    value = 0
    for row in numbers:
        for x in row:
            value += x
    return value 

print(sum(numbers[0]))
print(sum_nested(numbers))


# I originally wrote:
# def sum_nested(jkl):
# for row in sum_nested(numbers)
#   return sum(row) 
#, which didn't give me an error message but only added up the values
# in the third column (output was 6). I fixed it by adding a second for loop. This helped because
# the first for loops was only accessing the lists in the nested list, so I added the
# second one to access the items in each of those lists.

def five_by_five():
    fives = []
    counter = 1
    for i in  range(5):
        row = []
        for j in range(5):
            row.append(counter)
            counter += 1
        fives.append(row)
    return fives

print(five_by_five())
fivelist = five_by_five()

# I was getting an error saying saying "TypeError: 'int' object is not iterable" in lines 83 and 87.
# I fixed it by changing the value of counter from 0 to 1. I also had to deleted a variable within
# the function.
     
def multiples_of_3(fivelist):
    for row in fivelist:
        for item in range(len(row)):
            if row[item] % 3 == 0:
                row[item] = "?"
    return fivelist

print(multiples_of_3(fivelist))

not_equals_3 = fivelist

def sum_not_3(not_equals_3):
    value = 0
    for row in not_equals_3:
        for item in range((len(row))):
            if row[item] != "?":
                value += row[item]
    return value

print(sum_not_3(not_equals_3))

# Error: TypeError: not all arguments converted during string formatting
# This is because I made my list equal to multiples_of_3(fivelist) when fivelist had already changed.

# --- Dictionaries ---
# Dictionary Operations

ages = {
    "Katie": 30,
    "Mariam": 42,
    "Safia": 25,
    "Mira": 48
}

print(ages["Katie"])
ages.update({"Mira": 100})
print(ages)
ages.update({"Milana": 52})
print(ages)
del ages["Mariam"]
print(ages)

for key, value in ages.items():
    print(f"{key}: {value}")

# --- Running the Code ---
# Fav Function
print(sum_nested(numbers))





    




    


