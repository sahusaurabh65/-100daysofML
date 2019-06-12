#dunder methods 

class Employee:
    
    raise_amt =1.05
    
    def __init__(self,first,last,pay):
        self.first=first
        self.last= last
        self.email=first+'.'+last+"@email.com"
        self.pay = pay
        
    def fullname(self):
        return "{} {}".format(self.first,self.last)
    
    def apply_raise(self):
        self.pay = int (self.pay * self.raise_amt)
        
        
#unabigous representation of object and should be used for debugging,logging and thing like that  
    def __repr__(self):
        return "Employee('{}', '{}', '{}')".format(self.first, self.last, self.pay)
      
#readable representaion of object and used as display to end user 
    def __str__(self):
        return '{} - {}'.format(self.fullname(),self.email)
    
    def __add__(self ,other):
        return self.pay + other.pay
    
    def __len__(self):
        return len(self.fullname())
        
        
emp_1 = Employee("Corey","Schafer",5000)
emp_2 = Employee("Saurab","Sahu",  8000)
 


print (len(emp_1))
#print (emp_1 + emp_2)


#print(repr(emp_1))
#print(str(emp_1))
#
#print(emp_1.__repr__())
#print(emp_1.__str__())


