#constructor
#All class have a function called__init__(), which is always execuated when the class is being initiated.

class Student:
    def __init__(self,name,marks):
        self.name= name
        self.marks=marks
        print("adding new student in database..")
             

s1=Student("Ankit",97)
#print(s1.name, s1.marks)
print(s1.name, s1.marks)

s2=Student("Rahul",84)
print(s2.name,s1.marks)