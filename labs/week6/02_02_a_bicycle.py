"""
create a simple bicylce class

# Attributes
number of tires                             #i mean its a bicycle
type of of tires (road vs mountain bike)
model
color
number of speeds
brakes (front or back or both)
current speed.

# Methods
brake
pedal faster (should affect speed)
"""
class Bicycle:
    speedchange=1
    instance=0
    def __init__(self,type_of_tyres,model,color,number_of_speeds,brakes,current_speed):
        self.tyres=type_of_tyres
        self.model=model
        self.color=color
        self.speedvar=number_of_speeds
        self.brakes= brakes
        self.current_speed=current_speed

    def brake(self):
        if (self.speedvar>=self.current_speed>1):
            self.current_speed = self.current_speed - self.speedchange
       
        else :   
            pass
    def pedalfaster(self):
        if(self.current_speed>=0):
           self.current_speed = self.current_speed + self.speedchange
        elif(self.speedvar==self.current_speed):
            return "MAX SPEED"    
        else:
            pass 
    def instdetails(self):
        return f"the instance details are :tyre-{self.tyres} model-{self.model} color-{self.color} speed-{self.current_speed} spd types-{self.speedvar} brakes-{self.brakes}"                 


b1=Bicycle("Mountain","atlas","yellow",5,"both",0) 
print(b1.instdetails()) 

b1.pedalfaster()
#b1.brake()

print(b1.current_speed)

