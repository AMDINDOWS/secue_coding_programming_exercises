   




'''x = [10, [30, 'baz', 2.718], 'foo']

lst=[]
for i in x:
    if (type(i)==list) :
        lst.extend(i)
    else:
        lst.append(i)
   
#print(lst)


a = lst[2]

print(a[2])

def fun1(name, age): 
    print(name, age)'''

def multi_return(a, b, c):
      if a > 10:
             return b
      elif b> a:
              return c
      else:
             return a,b,c
z = multi_return(12,13,1)
print(z)

input_B = {4:"5",43:"342",72:"7"}





"""CLASS"""
class Thor:

    destination ="Asgard"

    def teleport(self):
        print("\n Lightning Teleport")

    def get_location(self):
        print(f"\n Thr location is : {self.destination}")

#1st obj(class instance), define object 
Mjonir=Thor()

Septre=Thor()

# value changing at object 
Mjonir.destination="Earth"

#class method calls, self para givrn but not req
Mjonir.teleport()

Mjonir.get_location()

Septre.teleport()

Septre.get_location()


aa="5502622159812088949850305428800254892961651752960000000000"
print(len(aa))

class Employee:
    numemp = 0
    raise_amt = 1.04 # a class variable
    def __init__(self,first,last,pay): #just like constructor and runs eveerytime like a flag counter can be used
        self.first=first #self.fname=first and similar to emp1.first="corey"
        self.last=last #these are class attributes i.e email , pay last etc.
        self.pay=pay
        self.email=first + '.' + last + '@company.com'
        Employee.numemp +=1 #used Employee. to not affected by instance
    
    def fullname(self):#this is a method
        return  f"the full name of employee : {self.first+self.last}"  # here use self.
    
    def payraise(self):
        self.pay= int(self.pay * self.raise_amt) #could also have used Employee.raise_amt and self gives the ability to change for that instance
        #self.pay= int(self.pay * 1.04) it cannot be updated for all (1.04) or can be accessed  

    def __repr__(self):
        return f"Employee({self.first},{self.last},{self.pay})"

    def __str__(self):
        return f"{self.fullname()} - {self.email}"
class Developer(Employee):
    raise_amt = 1.09 # this will not affect parent class
    def __init__(self,first,last,pay,prog_lang):
        super().__init__(first,last,pay)#still being handled by parent class Also use(Employee.__init__(self,first,last,pay))
        self.prog_lang=prog_lang

class Manager(Employee):
    def __init__(self,first,last,pay,employees=None):# never pass mutable as empty
        super().__init__(first,last,pay)#still being handled by parent class Also use(Employee.__init__(self,first,last,pay))
        if employees is None:
            self.employees=[]
        else:
            self.employees=employees
    def add_emp(self,emp):
        if emp not in self.employees:
            self.employees.append(emp)
    def remove_emp(self,emp):
        if emp in self.employees:
            self.employees.remove(emp)
    def print_emps(self):
        for emp in self.employees:
            print('--->', emp.fullname())








dev_1= Developer('Corey','Schafer',5000,"java") #passing based on init in employee, this is class instance, emp1 will be passed as (self)
dev_2= Developer('ts','us',500,'py')

dev_2.payraise()

print(dev_2.pay)

#print(help(Developer))# shows where is all in heritance

print(dev_1.email)#from main class
print(dev_1.prog_lang)# from sub class

mgr_1 = Manager('sue','Smith',9000,[dev_1])

print(mgr_1.email)

mgr_1.print_emps()

emp_1= Employee('Corey','Schafer',5000) #passing based on init in employee, this is class instance, emp1 will be passed as (self)
emp_2= Employee('ts','us',500)

print(emp_1)
print(emp_2)

#emp_1.first= "COrey"
#emp_1.last="JAson"
#emp_1.email="xx.y@com"
#emp_1.pay=300
print(f"the full name of employee : {emp_1.first+emp_1.last}")
print(emp_2.fullname())#as instance var#using method directly *self auto going.(#instance emp2 gets passed auto)
#also we can use below for same
print(Employee.fullname(emp_2))#as class var, using class directly and here instance is given as arguement (we have to tell the class what instance to use)
#emp_2.first="Ja"
#emp_2.last="kk"
#emp_2.email="xxjj@kom"
#emp_2.pay=899

print(emp_1.email)
print(emp_2.email)

#using class var rasie_amt
print(emp_2.pay)
emp_2.payraise()#applying the payraise method which has class variable
print(emp_2.pay)
#access raise_amt
print(Employee.raise_amt)
print(emp_1.raise_amt)#first checks instance attribute the checks in the class
print(emp_2.raise_amt)

#print(emp_1.__dict__)#namespace of emp 1
#print(Employee.__dict__)#namespace

Employee.raise_amt = 1.06 #change for all
emp_1.raise_amt= 1.05 # change for this instance ,breaks link , creates rasie_amt attb in emp1 namespace

print(Employee.raise_amt)
print(emp_1.raise_amt)
print(emp_2.raise_amt)

print(Employee.numemp)


# isinstace and issubclass

print(isinstance(mgr_1, Developer))
print(issubclass(Manager,Employee))

#special methods dunder
#__repr__ debug usage
#__str__ display end user readable


print(emp_1)
print(repr(emp_1))
print(emp_1.__repr__())

print(emp_1.__str__())


#*args(non keyword)is list (unpacks) and **kwargs(keyword) is dict (unpacks)

def adder(*num):
    sum = 0
    
    for n in num:
        sum = sum + n

    print("Sum:",sum)

adder(3,5)
adder(4,5,6,7)
adder(1,2,3,5,6)

def intro(**data):
    print("\nData type of argument:",type(data))

    for key, value in data.items():
        print("{} is {}".format(key,value))

intro(Firstname="Sita", Lastname="Sharma", Age=22, Phone=1234567890)
intro(Firstname="John", Lastname="Wood", Email="johnwood@nomail.com", Country="Wakanda", Age=25, Phone=9876543210)