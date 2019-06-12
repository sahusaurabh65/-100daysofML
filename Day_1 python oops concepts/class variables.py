#making class
class Employee:
    
    no_of_employees = 0
    rasie_amount =1.04 
    def __init__(self,first,last,pay):
        self.first=first
        self.last=last
        self.pay=pay 
        self.email=first + "."+last+"@company.com"
     
        Employee.no_of_employees += 1          #incrementing the number of employee
    
    def fullname(self):
        return "{} {}".format(emp_1.first,emp_1.last)
    
    def apply_rasie (self):
        self.pay=int(self.pay*self.rasie_amount)
    
#creating instance
emp_1 = Employee("corey","sahu",5000)
emp_2 = Employee("test","user",6000)
            
#output
#print(Employee.rasie_amount)
#print(emp_1.rasie_amount)
#print(emp_2.rasie_amount)

print(Employee.no_of_employees)


