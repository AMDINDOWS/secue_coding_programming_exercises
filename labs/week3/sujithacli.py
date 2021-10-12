# Build a CLI RPG game following the instructions from the course.
# Ask the player for their name.
name = input("Please enter your name: ")
# Display a message that greets them and introduces them to the game world.
print(f"Hello {name}! Welcome to the Game World!")
while True:
    print("Welcome to the Main Room: There are two doors - Left and Right")
    door = int(input("Please enter 1 for Left Door or 2 for Right Door: "))

    if door == 1:
        print("This is an empty room. Do you wish to look around the empty room or go back?")
        choice1 = int(input("Enter 1 to look around the room or 2 to go back to the Main Room: "))
        if choice1 == 1:
            print("You have found a Sword! Do you wish to take it?")
            wish1 = int(input("Enter 1 to take it or 2 to leave it: "))
            if wish1 == 1:
                print("You picked up the Sword!")
            else:
                print("You left the Sword!")
        else:
            break
    elif door==2:
        print("You encounter a Dragon! Do you wish to fight it or go back?")
        choice2 = int(input("Enter 1 to fight the Dragon or 2 to go back to the Main Room: "))
        if choice2 == 1:
            print("Do you have the Sword?")
            wish2 = input("Enter Y for Yes or N for No: ")
            if wish2 == 'Y':
                print("You have defeated the Dragon!!! You won!!!")
                break
            else:
                print("You have been defeated! You Lose!")
                break
        else:
            pass
    else:
        print("\nInVALID input")    