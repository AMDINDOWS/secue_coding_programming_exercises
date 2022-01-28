# make the most simple class possible


class Mobile:
    
    def __init__(self,brand,value):

        self.brand=brand #attribute
        self.value=value
    def instname(self):
        return  self.brand  
        

c1=Mobile("one plus", 47000) #instance

c2=Mobile("Nokia", 10000)

#print(Mobile.cellphone)
aa="5502622159812088949850305428800254892961651752960000000000"
print(len(aa))


    


# create an instance of your SimpleClass and print it out

c1=Mobile("one plus", 47000) #instance

c2=Mobile("Nokia", 10000)

print(c2.instname()) #printing instance 
# now add some functionality to your simple class


class LessSimpleClass:
    
    risinginst=0

    def __init__(self,fname,lname):
        self.first=fname
        self.last=lname
        LessSimpleClass.risinginst+=1
    
    def fulln(self):   
        self.full= self.first + self.last
        return self.full

n1=LessSimpleClass("Jackson","Michaels")
n2=LessSimpleClass("Jessy","Wilson")

print(n1.last)
print(LessSimpleClass.fulln(n1))
print(n1.fulln())

#class attb
print(n1.risinginst)
print(LessSimpleClass.risinginst)


    # add a class method


# print out your class attribute both from an instance of the class and through the class directly
# run the method - both directly from the class and through an instance.
