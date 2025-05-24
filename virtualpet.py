import os


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
    print(f"Welcome back! Your pet {name} missed you.")
else:
    name = input("Name your virtual pet: ")
    hunger = 5
    happiness = 5
    energy = 5
    level = 1
    coins = 0
    print(f"!You have adopted {name}! Take good care of it.")


def cat_face():
    print(r"""
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
    return f"{label}: [{bar}] ({value}/10)"

def show_status():
    cat_face()
    print("Pet Status:")
    print(status_bar("Hunger   ", hunger))
    print(status_bar("Happiness", happiness))
    print(status_bar("Energy   ", energy))
    print(f"# Level: {level}    $ Coins: {coins}")
    print(f"@ Mood: {get_mood()}")


while True:
    show_status()
    print("\nWhat would you like to do?")
    print("1. Feed (Cost 1 coin)")
    print("2. Play (Earn 1 coin)")
    print("3. Sleep")
    print("4. Save and Quit")

    choice = input("> ")

    if choice == "1":
        if coins >= 1:
            hunger = max(MIN_VALUE, hunger - 2)
            coins -= 1
            print(f"You fed {name}. (-1 coin)")
        else:
            print("X Not enough coins!")
    elif choice == "2":
        happiness = min(MAX_VALUE, happiness + 1)
        energy = max(MIN_VALUE, energy - 1)
        coins += 1
        print(f"You played with {name}. (+1 coin)")
    elif choice == "3":
        energy = min(MAX_VALUE, energy + 2)
        hunger = min(MAX_VALUE, hunger + 1)
        print(f"{name} had a good nap.")
    elif choice == "4":
        with open(pet_file, "w") as f:
            f.write(f"{name}\n{hunger}\n{happiness}\n{energy}\n{level}\n{coins}")
        print("Progress saved. See you next time!")
        break
    else:
        print("Please enter a number between 1 and 4.")


    if hunger >= 9:
        print("!Your pet is starving!")
    if energy <= 1:
        print("!Your pet is exhausted!")
    if happiness <= 2:
        print("!Your pet is unhappy. Play with it!")


    if hunger >= 10 or energy <= 0:
        print(f"{name} has fallen ill due to neglect...")
        print("Game over.")
        os.remove(pet_file)
        break


    if happiness >= 10:
        level += 1
        happiness = 5
        print(f"Congratulations! {name} has leveled up to Level {level}!")
