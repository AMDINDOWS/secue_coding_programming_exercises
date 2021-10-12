# write a short command line game

# 1. ask the user for their name: (use the input() function)

# Say hello to them with their name
# If their name begins with a vowel say something funny about that ("Aha! Oho! Uhu! Ihi! etc", your name begins with a vowel!)
# If their n ame begins with a consonant make an even better joke about it.

# Ask them to pick a number between 1 and 10.
# If they guessed the right number, tell them they won
# Else, tell them they lost.

import random
random_number = random.randint(0, 10)

name = input("Please Give Us your name(we wont share!!)" )
name1=name.lower()
print(f"\nYour name: {name1}")
if (name1[0] == "a")or( name1[0] =="e") or (name1[0] =="i") or (name1[0] =="o") or (name1[0] =="u") :
    print("\nViola vowel hmm interersing!")
else:
    print("\nFunny though no vowel u typed like a vowel guy")

print("\nNow time to pick a number between 1 to 10:")
number = int(input("\nPlease enter the number:"))

if number == random_number:
    print("YOU WON!!")
else :
    print("Lost sorry ")    


