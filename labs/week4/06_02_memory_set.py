# MEMORY GAME WITH SETS
# Continuously collect number input from a user with a `while` loop.
# Confirm that the input can be converted to an integer,
# then add it to a Python `set()`.
# If the element was already in the set, notify the user that their
# their input is a duplicate and deduct a point.
# If the user loses 5 points, quit the program.
# They win if they manage to create a set that has more than 10 items.

# you will need the `input()` function to collect information from the user

while True:
    num=int(input("\nEnter no : "))
    s1=set()
    flag=0
    if type(num)==int:
        print(type(num))
        s1.add(num)
        for i in range(0,len(s1)+1):
            if i in s1:
                print ("\nSAME SAME : YOU LOOSE A POINT")
                flag+=-1
                break
            else:
                continue
        if flag==5:
            
            print("\nYou lost")
            break
        elif len(s1)>10:
            print("\nYou won")
            break
                    



    elif type(num)!=int:
        print("input again pls(integers) : ")
        continue
        