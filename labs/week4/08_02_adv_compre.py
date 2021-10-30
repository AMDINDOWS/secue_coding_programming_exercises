# write code to generate a dictionary where
# each key is:an integer divisible by 3
# each value is: a list containing the even numbers in the range of key

# Take all the numbers divisible by 3 from 1-301
# example output
# {3: [2], 6: [2,4,6], 9:[2,4,6,8].... 300:[2,4,6,...288]}

dict1={i:[x for x in range(i+1) if x%2==0] for i in range(1,302) if i%3==0}

print(dict1)