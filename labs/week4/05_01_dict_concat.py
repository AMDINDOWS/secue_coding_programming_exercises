# Exercise

# Write a program to concatenate following dictionaries to create a new one.

# Sample Dictionary :
# dic1={1:10, 2:20}
# dic2={3:30, 4:40}
# dic3={5:50, 6:60}
# Expected Results: {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50, 6:60}
dic0={}
lst=[]

""""
i=0
while 0<i<=3:
    dic0.update(dict(i))
    i+=1

print(dic0)
"""
dic0.update(dic1)
dic0.update(dic2)
dic0.update(dic3)

print(dic0)