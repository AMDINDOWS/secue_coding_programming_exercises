# Type casting Exercise - 2
# Addition of string and integer using explicit conversion

# Initialise a string variable and integer variable
a = 10
b = "10"

exp_addn = a + int(b)
print("The value is after addition : " + f"{exp_addn}")

# After explicit conversion, use python to successfully perform
# the addition of these variables - print the result to the console
## Now try to convert this variable
c = "ten"
con_c1=float(c)
conv_c = int(con_c1)
print(type(conv_c))



## What kind of error does python give?
## What do you think the reason is?
# ANS : Because it's not a digital format so it cannot be mapped and further cannot be opearted upon.
