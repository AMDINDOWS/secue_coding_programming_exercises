# write rock-paper-scissors game

# have the user play against the computer
# you can use the random library to select an option for the computer

# use a while loop so the user can play until they win
import random
print("\nfor your knowledge Rock(1) Paper (2) scissor(3)")
print("\nlets play")
computer_choice = random.randint(1, 3)

while True:
    i = int(input("\nEnter your number to fight : "))
    if i == computer_choice :
        print("\nooh close one!!")
    elif (i != computer_choice) and (i == 3 or i ==2 or i==1) :
        if (i == 2 and computer_choice== 3) or (i==1 and computer_choice==2) or (i==3 and computer_choice==1):
            print("LOOSER!!!")
        elif  (i == 3 and computer_choice== 2) or (i==2 and computer_choice==1) or (i==1 and computer_choice==3): 
            print("WINNER WINNER !! Bye")
            break
    else:
        print("GO AGAIN!! HAHAHA")        




# you can map each of rock / paper / scissors to an integer from 1 - 3
