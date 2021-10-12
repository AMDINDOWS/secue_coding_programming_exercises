# Exercise

# Write an explicit infinite loop
# inside the infinite loop, read integer from user as an option

# If the option is 1: print here is your first step
# If the option is 2: print "you have some steps to go"
# If the option is 3: print "you are almost done"
# If the option is 4: quit from the loop

# If the option is other number: print it is an  invalid option
a=1
while bool(a):
    i = int(input("\nGive a number :"))

    if i == 1:
        print(" \nfirst step")
    elif i == 2:
        print("\nsome steps to go")    
    elif i==3:
        print("\nalmost there")
    elif i == 4:
        print("\ndone")
        break    
    else:
        print("\ninvalid")

