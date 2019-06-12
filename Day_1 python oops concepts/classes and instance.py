# python oop concepts 


#making class
class Employee:
    #defining 
    def __init__(self,first,last,pay):
        self.first=first
        self.last=last
        self.pay=pay 
        self.email=first + "."+last+"@company.com"
    
    def fullname(self):
        return "{} {}".format(emp_1.first,emp_1.last)
    
#creating instance
emp_1 = Employee("corey","sahu",5000)
emp_2 = Employee("test","user",6000)
            
#output
print(emp_1.fullname())    







#
#emp_1 = Employee()
#emp_2 = Employee()
#
#print( emp_1)
#print (emp_2)
#
#emp_1.first = "Coery"
#emp_1.last = "Sahu"
#emp_1.email = "coreysahu@gmail.com"
#emp_1.pay = 5000
#
#
#emp_2.first = "test"
#emp_2.last = "user"
#emp_2.email = "test.user@gmail.com"
#emp_2.pay = 5000
#
#
#print( emp_1.email)
#print (emp_2.email)


#print ("{} {}".format(emp_1.first,emp_1.last))
    
