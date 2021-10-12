# Logical_operators_4

# Initialize variable a to true, b to false and c to true
a = True
b = False
c = True
print("The value of a AND b OR c is: " f"{(a and b) or c}")
# Print the value of:
# what do you think: print(a and b or c)  will return? Why? # C true
# Does the order of operations matter?
# is print(a or b and c) different?
print("The value of a OR b AND c is: " f"{a or b and c}")
# Assign c to false and print the value of a and b or c
a = True
b = False
c = False
print("The value of a AND b OR c is: " f"{a and b or c}")
print("\nThe value of a AND (b OR c ) is: " f"{a and (b or c)}")
# Understand the difference in each scenario
# what is happening here?

# now try to use some ()'s to force python to evaluate it differently.
# we can change the operations.