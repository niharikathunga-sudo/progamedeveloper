#pythoninheirtance
#parentclass
class person:
    def __init__(self,name,adress,qualification):
        self.name=name
        self.adress=adress
        self.qualifcation=qualification
    
    def details(self):
        print("The details of the student are as shown below:")
        print("Name:",self.name)
        print("Adress:",self.adress)
        print("qualification:",self.qualifcation)
        
#childclass
class employee(person):
     def __init__(self,name,id,salary,adress,qualification):
        person.__init__(self,name,adress,qualification)
        self.id=id
        self.salary=salary
    
     def info(self):
        print("The details of the student are as shown below:")
        print("ID:",self.id)
        print("Salary:",self.salary)
        

person1=person("Niha","blue","worthy")
employee2=employee("Abhi","1675273","150K","blue","worker")

person1.details()

employee2.info()
        
employee2.details()