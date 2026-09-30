# Lists syntax
numbers = [1, 2, 3, 4]

print(numbers)

fruits = ["passion fruit", "star fruit", "apple", "orange"]
print(fruits)

mixed = ["Hello", 5, True, None]

print(mixed)

# access items in a list

print(numbers[1])

fruits[0] = "grape"
print(fruits)

# adding items
numbers.append(6)
print(numbers)

# insert item into list
print(mixed)
print(mixed.insert(1, False))
print(mixed)

# removing items
fruits.remove("apple")
print(fruits)
numbers.pop(2)
print(numbers)

# warmup
fav_colors = ["yellow", "teal", "pink"]
for color in fav_colors:
    print(color)

# ---Slicing---
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12] # define list
sub_nums = nums[1:4] # defines new list
print(sub_nums) # prints new lsit

# --- Striding ---
list = [12, 14, 16, 18, 20, 22]
list[::2]
print(list[1::2])
print(nums[1:8:2]) # starting number, stopping number, interval


