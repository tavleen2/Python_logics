class Employee:
    company = "HP"
    def __init__ (self,name,salary):
        self.name = name
        self.salary = salary

    #instance method (default)
    def print_info(self):
        info = f"The name is {self.name} and the salary is {self.salary}"
        print(info)

    #static method
    @staticmethod     
    def sum(a,b):
        return a+b
    
    #class method
    @classmethod
    def print_company(cls):
        print(cls.company)

    @classmethod
    def change_company(cls, new_company):
        cls.company = new_company

e1 = Employee("Jack", 234)
e2 = Employee("John", 334)
# print(Employee.company)
# print(Employee.name)   #Error: class has no attribute 'name'
e1.print_info()
e2.print_info()
print(e2.sum(2,4))
e1.print_company()
e1.change_company("Dell")
e1.print_company()
print(Employee.company)