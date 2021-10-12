name = input("Enter your name: ")
print(f"Welcome to CLI RPG, {name}")
while input("Do u want to play? answer yes or no: ") == 'yes':
    print("You are in the main room")
    print("You can choose between two doors to play, 1 for left and 2 for right")
    choice = int(input("Enter your choice: "))
    while choice == 1:
        print("You are in an empty room. Do you want to look for the sword or go back to the room")
        choice1 = int(input("Enter 1 to go back or 2 to look for the sword: "))
        if choice1 == 1:
            break
        else:
            answer1 = input("Did u find the sword? answer yes or no: ")
            if answer1 == 'yes':
                answer11 = input("do want to take it or leave it? answer 'take' or 'leave': ")
                if answer11 == 'take':
                    print("sword taken")
                    break
                else:
                    print("sword not taken")
                    break
            else:
                print("keeping looking!")
    while choice == 2:
        print("You have encountered a dragon. Do u want to fight or go back to the room?")
        choice2 = int(input("Answer 1 to go back and 2 to fight: "))
        if choice2 == 1:
            break
        else:
            answer2 = input("Do u have the sword? answer yes or no: ")
            if answer2 == 'yes':
                print("You can defeat it")
                break
            else:
                print("You will get eaten")
                break