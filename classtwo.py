class People:
    def __init__(self, Name, Gender, Age):
        self.myname = Name
        self.mygender = Gender
        self.myage = Age

    def display(self):
        print(self.myname, self.mygender, self.myage)


# object
myobj = People("Nicholus", "Male", 20)
myobj.display()

myobj = People("Brian", "Male", 22)
myobj.display()

myobj = People("Faith", "Female", 21)
myobj.display()
