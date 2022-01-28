# You start this journey with a number `n`.
# You have to display a string representation of all numbers from 1 to n,
# but there are some constraints:
# - If the number is divisible by 3, write `Fizz` instead of the number
# - If the number is divisible by 5, write `Buzz` instead of the number
# - If the number is divisible by both 3 and 5, write `FizzBuzz` instead of the number

# feel free to adjust n for debugging
n = 100
store=" "
for i in range(n):
    if (i % 3==0):
        print(f"\nFizz : {i}")
        store = store + (" Fizz ")
    if (i % 5==0):
        print(f"\nBuzz : {i}")
        store = store + (" Buzz ")
    if (i % 3==0) and (i % 5==0):
        print(f"\nFizzBuzz : {i}")
        store = store + (" FizzBuzz ")
    else:
        print(i)
        store = store + " " +str( i )    
    
print(store)

