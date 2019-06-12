#import library
import datetime


#making class
class Employee:
    
    no_of_employees = 0
    rasie_amount =1.04 
    def __init__(self,first,last,pay):
        self.first=first
        self.last=last
        self.pay=pay 
        self.email=first + "."+last+"@company.com"
     
        Employee.no_of_employees += 1   #incrementing the number of employee
    
    def fullname(self):
        return "{} {}".format(emp_1.first,emp_1.last)
    
    def apply_rasie (self):
        self.pay=int(self.pay*self.rasie_amount)
    
    @classmethod
    def set_rasie_amt(cls,amount):
        cls.rasie_amount = amount 
    @classmethod
    def from_string(cls,emp_str):
        first,last,pay = emp_str.split ("-")
        return cls(first,last,pay)
    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() ==6:
            return False
        return True
    
#creating instance 
emp_1 = Employee("corey","sahu",5000)
emp_2 = Employee("test","user",6000)
    
#data time 
my_date = datetime.date(2016,7,11)
print (Employee.is_workdaymy_date(my_date))
           
############usecase#########################
#emp_str_1 = 'John-doe-23000'
#emp_str_2 = 'steve-smith-3000'
#emp_str_3 = 'Jane-doe-9000'
##first,last,pay = emp_str_1.split ("-")
#new_emp_1 = Employee.from_string(emp_str_1)
#print(new_emp_1.email)
#print(new_emp_1.pay)
#


##########additional constuructors######33
 
















