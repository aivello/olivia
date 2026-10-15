'''
--- Dictionaries
Lists, key-value pairs separated by commas
key and value separated by colons

Mutable: changable
'''

# --- Example ---
star = {
    "name": "Vega", 
    "magnitude": "0.57", 
    "distance": "25.05" # light years
}

for key in star.keys():
    print(key)

list1 = list(range(0, 11))
print(list1)

print(list1[0:4:])
print(list1[0::2])
print(list1[::-1])

a = [2, 4, 6]
b = [8, 10, 12]
c = [14, 16, 18]
nested_list = [a, b, c]
print(nested_list)

'''
nested_list = [[2, 4, 6]
               [8, 10, 12]
               [14, 16, 18]]
print(nested_list[2][1])
# not working
'''

stars_data = {
    "name": ["Sirius", "Vega", "Altair"],
    "magnitude": [-1.46, 0.03, 0.77],
    "distance_ly": [8.6, 25.0, 16.7],
    "constellation": ["Canis Major", "Lyra", "Aquila"]
}

for star in stars_data["name"]:
    print(star)

def stars_data(stars_data):
    count = 0
    for distance in stars_data["distance_ly"]:
        if distance < 20:
            count += 1
    return count

print(stars_data(stars_data))