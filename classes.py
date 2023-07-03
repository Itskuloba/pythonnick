class Magari:
    def __init__(self,modelname,color,year,capacity):
        self.model=modelname
        self.mycolor=color
        self.myyear=year
        self.itscapacity=capacity
    def onyesha(self):
        print(self.model,self.mycolor,self.myyear,self.itscapacity)
#create an object
myobj=Magari("Toyota","White",2020,"2000cc")
myobj.onyesha()

myobj=Magari("Nissan","Black",2022,"2500cc")
myobj.onyesha()