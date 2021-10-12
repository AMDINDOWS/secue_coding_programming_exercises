# Exercise

# Write a python program to print all prime numbers between 0 to 100 , and print how many prime numbers are there
# if you don't know an algorithm to check for primes
# ask Dr. Kurunandan Sir
# google it

'''''
for i in range (2,101):
    counter = 0
    for j in range(2,int((i/2)+1)): # or floor division (//)
            if (i%j)==0:
                counter +=1
    if counter ==0:
            print(f"PRIME : {i}")        
 '''               
        
               
print("Prime numbers are")

for num in range(0,101):

    if num>1:

        for i in range (2, num):

            if (num % i) == 0:

                break

        else:

             print(num)

a = num.count()

print(a)    