# Making a class
class Employee:
    # special method/megic method/dander method - constructor
    def __init__(self):
        # instance variables
        print('enter a detalils')
        self.name = "Hridoy Khan"
        self.age = 23
        self.salary = 50000
        
# Creating an object
emp = Employee()
# Accessing instance variables
print(emp.name)