import os
import random

MAX_VALUE = 10
MIN_VALUE = 0
pet_file = "pet_save.txt"

if os.path.exists(pet_file):
    with open(pet_file, "r") as f:
        lines = f.readlines()
        name = lines[0].strip()
        hunger = int(lines[1])
        happiness = int(lines[2])
        energy = int(lines[3])
        level = int(lines[4])
        coins = int(lines[5])
    print("Welcome back! Your pet " + name + " missed you.")
else:
    name = input("Name your virtual pet: ")
    hunger = 5
    happiness = 5
    energy = 5
    level = 1
    coins = 0
    print("You have adopted " + name + "! Take good care of it.")

weather = random.choice(["Sunny", "Rainy", "Windy", "Snowy"])

def cat_face():
    print("""
 /\_/\  
( o.o ) 
 > ^ < 
""")

def get_mood():
    if hunger >= 9 or energy <= 2:
        return "Unwell"
    elif happiness >= 8:
        return "Happy"
    elif happiness <= 3:
        return "Sad"
    else:
        return "Normal"

def status_bar(label, value):
    bar = "*" * value + "-" * (MAX_VALUE - value)
    return label + ": [" + bar + "] (" + str(value) + "/10)"

def show_status():
    cat_face()
    print("Weather: " + weather)
    print("Pet Status:")
    print(status_bar("Hunger", hunger))
    print(status_bar("Happiness", happiness))
    print(status_bar("Energy", energy))
    print("Level: " + str(level) + "    Coins: " + str(coins))
    print("Mood: " + get_mood())

def pet_talk():
    mood = get_mood()
    if mood == "Happy":
        print(name + " says: I'm so happy with you!")
    elif mood == "Sad":
        print(name + " says: I feel a bit lonely...")
    elif mood == "Unwell":
        print(name + " says: I don't feel well...")
    else:
        print(name + " says: Let's do something fun today!")

def random_event():
    events = ["toy", "spoiled_food", "coin", "sick", "energy_boost", "none"]
    event = random.choice(events)
    result = {}
    if event == "toy":
        print("Your pet found a toy! +2 happiness, +1 coin.")
        result["happiness"] = 2
        result["coins"] = 1
    elif event == "spoiled_food":
        print("The food was spoiled. -1 hunger, -1 energy.")
        result["hunger"] = -1
        result["energy"] = -1
    elif event == "coin":
        print("You found a coin! +1 coin.")
        result["coins"] = 1
    elif event == "sick":
        print("Your pet got a cold. -2 energy.")
        result["energy"] = -2
    elif event == "energy_boost":
        print("Nice weather! Your pet feels refreshed. +2 energy.")
        result["energy"] = 2
    return result

def check_achievements():
    if coins >= 10:
        print("Achievement: Rich Cat!")
    if level >= 3:
        print("Achievement: Level 3 Pet!")

while True:
    show_status()
    pet_talk()
    check_achievements()

    print("\nWhat would you like to do?")
    print("1. Feed (Cost 1 coin)")
    print("2. Play (Earn 1 coin)")
    print("3. Sleep")
    print("4. Clean")
    print("5. Talk")
    print("6. Adventure")
    print("7. Save and Quit")

    choice = input("> ")

    if choice == "1":
        if coins >= 1:
            hunger = max(MIN_VALUE, hunger - 2)
            coins -= 1
            print("You fed " + name + ".")
        else:
            print("Not enough coins!")
    elif choice == "2":
        happiness = min(MAX_VALUE, happiness + 1)
        energy = max(MIN_VALUE, energy - 1)
        coins += 1
        print("You played with " + name + ".")
    elif choice == "3":
        energy = min(MAX_VALUE, energy + 2)
        hunger = min(MAX_VALUE, hunger + 1)
        print(name + " had a good nap.")
        event = random_event()
        hunger = max(MIN_VALUE, min(MAX_VALUE, hunger + event.get("hunger", 0)))
        happiness = max(MIN_VALUE, min(MAX_VALUE, happiness + event.get("happiness", 0)))
        energy = max(MIN_VALUE, min(MAX_VALUE, energy + event.get("energy", 0)))
        coins += event.get("coins", 0)
        weather = random.choice(["Sunny", "Rainy", "Windy", "Snowy"])
    elif choice == "4":
        print("You cleaned " + name + " nicely.")
        happiness = min(MAX_VALUE, happiness + 2)
        energy = max(MIN_VALUE, energy - 1)
    elif choice == "5":
        print(name + " says: Thanks for the talk!")
        happiness = min(MAX_VALUE, happiness + 1)
    elif choice == "6":
        print(name + " went on an adventure!")
        energy = max(MIN_VALUE, energy - 2)
        result = random.choice(["coin", "nothing", "tired"])
        if result == "coin":
            print("Found a coin! +1 coin.")
            coins += 1
        elif result == "tired":
            print("Got tired from the trip. -1 energy.")
            energy = max(MIN_VALUE, energy - 1)
        else:
            print("Nothing special happened.")
    elif choice == "7":
        with open(pet_file, "w") as f:
            f.write(f"{name}\n{hunger}\n{happiness}\n{energy}\n{level}\n{coins}")
        print("Progress saved. Bye!")
        break
    else:
        print("Please enter a number between 1 and 7.")

    hunger = min(MAX_VALUE, hunger + 1)
    happiness = max(MIN_VALUE, happiness - 1)
    energy = max(MIN_VALUE, energy - 1)

    if hunger >= 9:
        print("Your pet is starving!")
    if energy <= 1:
        print("Your pet is exhausted!")
    if happiness <= 2:
        print("Your pet is unhappy!")

    if hunger >= 10 or energy <= 0:
        print(name + " got too sick...")
        print("Game over.")
        if os.path.exists(pet_file):
            os.remove(pet_file)
        break

    if happiness >= 10:
        level += 1
        happiness = 5
        print("Congrats! " + name + " reached Level " + str(level) + "!")
