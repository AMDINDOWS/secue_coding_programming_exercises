print("The program to say time of day")

time = int(input("\nPlease enter the time :"))

if  600 <= time < 1200 :
    print(" Good Morning")
elif 1200 == time  :
    print(" Its noon my friend")
elif 1200 < time <= 1700 :
    print("Its afternoon")
elif 1700 < time < 2000 :
    print("Evening mate")
elif (2000 <= time < 5990 ) or (time == 0) :
    print(" What a beautiful nght")
else :
    print("Invalid Time!!")

