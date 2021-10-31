# Exercise

# Write a program to create a dictionary from a string.
# Track the count of the letters from the string.
# Sample string : 'securecoding'
# Expected output: {'s': 1, 'e': 2, 'c': 2, 'u': 1, 'r': 1, 'o': 1, 'd': 1, 'i': 1, 'n': 1, 'g': 1}

st1='securecoding'

dict1={i:st1.count(i) for i in st1 for i in st1}
print(dict1) 

