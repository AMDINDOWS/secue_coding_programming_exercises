# write a script that will "sing" a song that goes like this
#  "there are 100 jars of payasam on the counter ...... now i ate one!"
# "there are 99 jars of payasam on the counter ... now I ate one!"
#
#
# "there are 0 jars of payasam on the counter - none left to eat!"
# "now I will go vomit...."

# you must use a while loop to do it
i=0
while i <= 100:
    if i <=99:
        print(f"\nthere are {100-i} jars of payasam on the counter ...... now i ate one!")
    else :
        print("\nthere are 0 jars of payasam on the counter - none left to eat!")   
    i+=1     
