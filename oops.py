"""def name():
    print("HIIIII IM AKSHAYA AND I WILL BE HELPING YOU TODAYYYY!!!!!")
    user=input("Whats your name?")
    print(f"Hey {user} I'll be working with you today!!!")

name()"""


class student:
    #constructor function
    def __init__(self,name,age,house):
        self.name=name
        self.age=age
        self.house=house
        self.grade="9"
        self.teacher="Ms.Thunga"

    def showurself(self):
        print("The details of the student are as shown below:")
        print("Name:",self.name)
        print("Age:",self.age)
        print("Grade:",self.grade)
        print("House:",self.house)
        print("Teacher:",self.teacher)
    
student1=student("niha","14","blue")
student2=student("abhi","3 months","blue")

student1.showurself()
student1.age=15
student1.showurself()
print(student1.teacher)

student2.showurself()
