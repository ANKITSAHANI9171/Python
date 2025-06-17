#create student classs that takes name & marks of 3 subjects as arguments in constructor.
#then create a method to print the average.

class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks

    def get_avg(self):
        sum=0
        for val in self.marks:
            sum+= val
        print("hi", self.name, "your avg score is:", sum/5)
s1=Student("Ankit", [99,98,96,85,80])
s1.get_avg()

s1.name="name"
s1.get_avg()