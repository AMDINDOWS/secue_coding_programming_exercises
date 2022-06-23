"""
create a chicken class that has the following

# class attributes
time_of_day
number_of_eggs_laid

# instance attributes (uses the self variable)
breed
gender
weight
lays_eggs (boolean)

# methods
lay_egg --> this function should depend on time of day (chickens only lay eggs at night!),
it should also use random numbers to deterimine if laying the egg worked or not


## Create 100 instances of your chickens using a for loop

Use a for loop to update the time of day (go through each hour of the day)
within the loop have your chickens all try to lay eggs
Afterwards, print out how many total eggs were hatched -- for all chickens and individually.
What was the average number of eggs per chicken?
"""

import random

time=["DAY","NIGHT"]
b_breed=["B","R","E","E","E","D"]
g_gender=["MALE","FEMALE"]
W_weight=[90,89,78,56,45]

class Chickens:
    time_of_day =''
    number_of_eggs_laid=0
    instchicken=0
    
    def __init__(self,breed,gender,weight,lays_eggs):
        self.breed =breed
        self.gender=gender
        self.weight=weight
        self.lays_eggs=bool(lays_eggs)
        Chickens.time_of_day=random.choice(time)
        Chickens.instchicken+=1

    def lay_egg(self):
        if (Chickens.time_of_day=="NIGHT" and self.gender=="FEMALE EGG"):
            self.lays_eggs=True
            Chickens.number_of_eggs_laid+=1
        else:
            self.lays_eggs=False    

        

for z,i in enumerate(range(0,100)):
    chik_i = Chickens(random.choice(b_breed),random.choice(g_gender),random.choice(W_weight),False) 
    #print(f"{z} {chik_i.lays_eggs}")
    if z==1:
        print(chik_i.weight)

print(Chickens.instchicken)
print(Chickens.number_of_eggs_laid)
