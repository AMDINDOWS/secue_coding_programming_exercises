# make the most simple class possible


class Mobile:
    cellphone=0
    def __init__(self,brand,value):

        self.brand=brand #attribute
        self.value=value
        Mobile.cellphone+=1

c1=Mobile("one plus", 47000) #instance

c2=Mobile("Nokia", 10000)

print(Mobile.cellphone)



    


# create an instance of your SimpleClass and print it out


# now add some functionality to your simple class


class LessSimpleClass:
    pass
    # add one class attribute

    # add a class method


# print out your class attribute both from an instance of the class and through the class directly
# run the method - both directly from the class and through an instance.
