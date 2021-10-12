# Exercise

num_one = 10
num_two = 2
num_three = 1010
num_four = 123

# Use if / else statement to find the largest number.
if num_one > num_two :
    if num_one > num_three:
        if num_one > num_four:
            print("largest is num_one")
        else:
            print("num_four largest")    
    else:
        if num_three> num_four:
            print("num_three is largest")
        else:
            print("num_four largest")
else:
    if num_two > num_three:
        if num_two> num_four:
            print("num_two largest")
        else:
            print("num_four largest")
    else:
        if num_three>num_four:
            print("num_three is largest")
        else :
            print("num_four largest")    