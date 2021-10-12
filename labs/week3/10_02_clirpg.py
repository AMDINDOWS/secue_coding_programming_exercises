# Build a CLI RPG game following the instructions from the course.

# Ask the player for their name.

# Display a message that greets them and introduces them to the game world.

# Present them with a choice between two doors.

# If they choose the left door, they'll see an empty room.

# If they choose the right door, then they encounter a dragon.

# In both cases, they have the option to return to the previous room or interact further.

# When in the seemingly empty room, they can choose to look around. If they do so, they will find a sword. They can choose to take it or leave it.

# When encountering the dragon, they have the choice to fight it.

# If they have the sword from the other room, then they will be able to defeat it and win the game.

# If they don't have the sword, then they will be eaten by the dragon and lose the game.
name = input("\nPlease enter your name: ")

print(f"\n Welcome to Jumanji {name} , dont worry you will not die  ")

print("\nChoose your Door")
flag=0
while True:
    
    door=input("\nPlease Choose Left or Right Door Enter L for Left and R for Right: ")

    if (door == "L"):
        print("\nTHIS ROOM IS EMPTY , DO YOU WISH TO EXPLORE? ENTER Y for yes and N for No")

        explore = input("\nWHAT IS YOUR ANSWER : ")
        if explore == "Y":
            print("\nYou found a sword do you wish to take it yes(Y) and No(N)")
            sword =input("\nTAKE OR NO ?: ") 
            if sword == "Y" :
                flag = 1
                print("\nYou weild the power of lightsaber")
            elif sword == "N":
                print("\nNO SWORD")
                continue
            else:
                print("\n How will you save jumanji If you cant read instructions properly? :(invalid input) ")
        elif explore == "N":
            print("\n Back to rooms")
            continue
        else:
            print("\n Read the instructions again (invalid input)")            
    elif door == "R":
        print("\nRAAA DRAGON HERE DO YOU WISH  To fight")
        fight = input("\nFight yes (Y) no (N) : ")
        if (fight == "Y") and (flag == 1):
            print("\nYOU WON HE DIED BRAVOO!!")
            print("\nThanks for playing and Saving Jumanji")
            break
        elif(fight == "Y") and (flag != 1):
            print("\nYOU DIED")
            print("\nThanks to play!!")
            break
        elif(fight == "N") :
            print("\nBack to rooms")
            continue
        else:
            print("\nInvalid input")    
    else:
        print("\nInvalid Input warning!!")
