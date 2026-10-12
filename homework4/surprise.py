# File: surprise.py

# Below is a dictionary of targets you want to observe.

# If you are an observational astronomer or instrumentalist, picking the correct targets
# to point the telescope at is very important. Let's practice below.

targets = {
    "Vega": {
        "RA": "18h 36m 56.3s",
        "Dec": "+38° 47′ 01″",
        "Magnitude": 0.03,
        "Spectral Type": "A0Va"
    },
    "Betelgeuse": {
        "RA": "05h 55m 10.3s",
        "Dec": "+07° 24′ 25″",
        "Magnitude": 0.42,
        "Spectral Type": "M1-M2 Ia-Ib"
    },
    "Sirius": {
        "RA": "06h 45m 08.9s",
        "Dec": "−16° 42′ 58″",
        "Magnitude": -1.46,
        "Spectral Type": "A1V"
    },
    "Rigel": {
        "RA": "05h 14m 32.3s",
        "Dec": "−08° 12′ 06″",
        "Magnitude": 0.12,
        "Spectral Type": "B8Ia"
    },
    "Polaris": {
        "RA": "02h 31m 49.1s",
        "Dec": "+89° 15′ 51″",
        "Magnitude": 1.97,
        "Spectral Type": "F7Ib"
    }
}

# --- Questions ---
# 1) Write a function that uses a loop to print the name of each star.
def star_name(targets):
    for key in targets.keys():
        print(key)

print(star_name(targets))

# 2) Write a function that uses a loop to print the name of each star with its spectral type.
def spectral_type(targets):
    for item in targets:
        print(item, targets[item]["Spectral Type"])

print(spectral_type(targets))

# 3) Write a function that uses a conditional to find stars with magnitudes greater than 0.1 mag.
def magnitudes(targets): 
    for item in targets:
        if (targets[item]["Magnitude"]) > .1:
            print(item, targets[item]["Magnitude"])

print(magnitudes(targets))

# 4) Look up another target, add all the necessary information to the targets list. 

targets.update({"Acrux": 
                {"RA": "12h 26m 35s",
                 "Dec": "−63° 05′ 56.7″",
                 "Magnitude": 0.77,
                 "Spectral Type": "B1V"}})

print(targets)

# 5) Write a function that finds the brightest star whose Declination is closest to 20°.
def brightest_star_dec20(targets):
    brightest = list(targets.keys())[0]
    for item in targets:
            if targets[item]["Magnitude"] < targets[brightest]["Magnitude"]:
                brightest = item 
    return brightest

print(brightest_star_dec20(targets))


# 6) What is your favorite constellation?
# Ursa Major


