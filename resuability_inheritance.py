#resuability - inheritance
"""
Inheritence :

Inheritance is the principal of inherting attributes and methods present in a
parent class to the child class

"""

'''
#Employee , student
#employee - mentor , counseller


#commom property for employee and student are
#id, name, phno


class person:#base class , parent class , super class
    def __init__(self, i_d, name, phno):
        self.id_num = i_d
        self.name = name
        self.ph_no = phno
    def display(self):
        print("***personal details***")
        print(f"ID : {self.id_num}")
        print(f"Name : {self.name}")
        print(f"Phone : {self.ph_no}")

class Employee(person):#inheriting
    pass   #since i want to details to be printed as in display
emp = Employee("1234","sai",8994833857)
print(emp.id_num)
emp.display()





# if i want add another attribute
class person:#base class , parent class , super class
    def __init__(self, i_d, name, phno):
        self.id_num = i_d
        self.name = name
        self.ph_no = phno
    def display(self):
        print("***personal details***")
        print(f"ID : {self.id_num}")
        print(f"Name : {self.name}")
        print(f"Phone : {self.ph_no}")

class Employee(person):#inheriting
    def __init__(self, name, ph_no, id_no, role):
        #since super class has (name , ph_no , id ) here i onlu want to assign role
        # hence we are calling constructor using super keyword
        super().__init__(name, ph_no, id_no)#super acts as self
        self.role = role
    def employee_display(self):
        super().display()
        print(f"Role :  {self.role}")
#emp = Employee("1234","sai",8994833857)#TypeError: Employee.__init__() missing 1 required positional argument: 'role'
emp = Employee("1234","sai",8994833857,"data_analytics")
emp.employee_display()
'''



# if i want to inherit more
class person:#base class , parent class , super class
    def __init__(self, i_d, name, phno):
        self.id_num = i_d
        self.name = name
        self.ph_no = phno
    def display(self):
        print("***personal details***")
        print(f"ID : {self.id_num}")
        print(f"Name : {self.name}")
        print(f"Phone : {self.ph_no}")

class Employee(person):#inheriting
    def __init__(self, name, ph_no, id_no, role):
        #since super class has (name , ph_no , id ) here i onlu want to assign role
        # hence we are calling constructor using super keyword
        super().__init__(name, ph_no, id_no)#super acts as self
        self.role = role
    def employee_display(self):
        super().display()
        print("***Employee Details:***")
        print(f"Role :  {self.role}")
class college:
    def __init__(self,clgname,dept):
        self.clgname = clgname
        self.dept = dept
    def college_Details(self):
        print("***Academic details:***")
        print(f"College Name: {self.clgname}")
        print(f"Department : {self.dept}")

class Student(person, college):#inpython a class can inherit 2 or more than 2 class in any order
    def __init__(self, id_num, name, phno, clgname, dept):
        #super().__init__(id_num, name , phno)
        #super().__init__(clgname, dept)
        '''
#stu1 = Student(123,"joy",9381388304,'X','CSE')
File "E:\python_programs\resuability_inheritance.py", line 102, in __init__
super().__init__(clgname, dept)
TypeError: person.__init__() missing 1 required positional argument: 'phno'
'''
        

        person.__init__(self,id_num, name , phno)
        college.__init__(self,clgname, dept)
    def student_detail(self):
        person.display(self)
        college.college_Details(self)
class Mentor(Employee):
    def __init__(self, id_num, name, ph_no, role, batches):
        super().__init__(id_num, name, ph_no, role)
        self.batches = batches

    def mentor_detail(self):
        self.employee_display()
        print("*** Mentor Details ***")
        print(f"Batches : {self.batches}")

        
stu1 = Student(123,"joy",9381388304,'X','CSE')
stu1.student_detail()

mentor1 = Mentor(456, "Riya", 9876543210, "Python Trainer", ["Batch A", "Batch B"])
mentor1.mentor_detail()

#here checking which constructor obj should be created such that it print output , but it throws error
#stu1 = Student(763,"joy",9392849472,"X","CSE")#TypeError: person.__init__() takes 4 positional arguments but 6 were given
#MRO - method resolution order
'''
class Student(person, college): MRO(left - right) means first it check the Student class and then person class and college
When a class inherits from multiple classes (like Student(person, college)), Python uses MRO to decide which method or constructor to call first.
🔍 How MRO works:
- Python looks left to right in the inheritance list.
- So in class Student(person, college), Python first checks Student, then person, then college.
- It uses the C3 linearization algorithm to create a consistent order.
You can view the MRO of any class using:
print(Student.__mro__)
'''








