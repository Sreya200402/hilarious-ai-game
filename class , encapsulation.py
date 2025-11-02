
#banking system # procedural programming
acc_1_no = 9855877822
acc_1_no = 'sreya'
acc_1_balance = 10000

def withdraw(amount, acc_no, balance):
    if amount <= balance:
        print("amount withdrawn")
        balance -= amount # when we pass mutable object to function it bahave as pass by reference
        # when we pass immutable object to the function it behavious as pass by value
        # here balance is int(immutable) even after updating the value wont be updated
        return balance # the value returned and updating to new assignment
    else:
        print("amount cannot be withdrawn -- insufficient funds")
        return balance # return same as balance as 10000
def deposit(amount, acc_no, balance):
    if amount > 0:
        print("Deposited successfully")
        balance += amount
    return balance
withdraw()
'''
⚠️ Drawbacks of POP (compared to OOP) Here’s a breakdown of the limitations of POP, especially as your project grows:
- Scattered Data and Logic
- Data (acc_no, balance) and logic (withdraw, deposit) are separate.
- You have to pass the same data around repeatedly.
- No Encapsulation
- Anyone can access or modify balance directly.
- There’s no protection or control over how data is used.
- Harder to Scale
- Adding features like transaction history, multiple accounts, or user authentication becomes messy.
- You’d need more global variables or complex - parameter passing.
- Code Duplication
- You might repeat similar logic across functions.
- No concept of inheritance or reuse like in OOP.
- Poor Real-World Mapping
- Real-world entities like “Account” or “Customer” aren’t modeled as objects.
- It’s harder to think in terms of “things” and their behaviors.
✅ When POP is Still Useful
- For small scripts or simple tasks like your current ATM simulation.
- When performance is critical and object overhead is unnecessary.
- For learning foundational logic before diving into OOP. concise it so I can understand make sure even thiree year child can understand by concise it
'''

    
'''
when you want to define user defined datatypes it can be possible using 'class'
'''
        
    

class account:
    def __init__(self,acc_no,acc_name,acc_bal):#address of acc_1,arguments         # constructor
        self.acc_no=acc_no
        self.acc_name=acc_name
        self.acc_bal=acc_bal
    def withdraw(self,amount): # the function name can be any name 
        if self.acc_bal>amount:
            print("withdrawn")
            self.acc_bal-=amount
        else:
            print("insufficient funds")
    def deposit(self,amount):
        if amount>0:
            self.acc_bal+=amount
            print("deposited")
        else:
            print("amount should be valid")
acc_1=account(9876543210,"kusum",10000)
acc_2=account(1234567890,"sriya",50000)
print(acc_1.acc_name)
print(acc_2.acc_bal)
acc_2.withdraw(1000)
print(acc_2.acc_bal)
print(acc_1.acc_bal)
acc_1.deposit(1000)
print(acc_1.acc_bal)



#write a class represent student details
#name , mail , idno (instance object) - objects are differ from one another 
#display_details , grade(marks)
class student:
    def __init__(self, name, mail, id_no):#instance attributes
        self.name = name
        self.mailid = mail
        self.idno = id_no
    def display_details(self):
        print(f"Name is: {self.name}")
        print(f"Email id : {self.mailid}")
        print(f"id_no : {self.idno}")
    def grade(self, marks):
        if marks > 90:
            return f"{self.name} got 'A' grade"
        elif marks > 70 :
            return f"{self.name} got 'B' grade"
        else:
            return f"{self.name} got 'C' grade"

student1 = student('X','x@gmail.com',123)
student1.display_details()
print(student1.grade(90))





#different types of constructor
'''
here __init__ is a constructor , self is the object to represent the constructor
above __init__(self, name, mail, id_no): #here other than self every thing i.e name,mail,idno are known as "parameterized constructor"
there are default constructor  without parameters other than 'self' the above is the example
'''

class batch:
    def __init__(self): #only one parameter i.e self is known as default constructor
        self.students = []   
    def add_student(self, student_name):#methods
        self.student.append(student_name)
    #def students(Self): # already defined objects may occur conflict like construct as 'students' an object here we defining again as students may rise conflict
    def print_students(self):
        for i in self.students:
            print(i)
DS19 = batch()
print(DS19.students)#an empty list
DA18 = batch()
print(DA18.students)#an empty list


#instance attribute are the unique for every object in a class which we define  with __init__ can be accessed using objects only
#class attributes are the attributes which are same from every one in a class  which is defined inside the class outside the method
#these class attribute accessed using object or class 
class student:
    institute = 'Codegnan' #class attributes
    location = 'hyderabad' #class attribute
    def __init__(self, name, mail, id_no):#instance attributes
        self.name = name
        self.mailid = mail
        self.idno = id_no
    def display_details(self):
        print(f"Name is: {self.name}")
        print(f"Email id : {self.mailid}")
        print(f"id_no : {self.idno}")

student1 = student('Bob','B@gmail.com',1234)
print(student1.institute)#class attribute accessing using object 
print(student.institute)# class attribute accessing using class

#how to prevent others to access the variables when they are 'global' which can be done using 'Access Modifiers'
#in python even though we use access modifiers are issued using data manipulation we can access private and protected variables


#Access Modifiers : denoted using underscore(_) at the begining of the name or function
'''
1 . public - no underscore at the begining of the name 
2 . protected - single underscore at the begining of te name tells that it is a protected member.
                it is just a convention to mention particular member is protected do not try to modify it until or unless it is very necessary
                i.e we are using _ in the name but can be used any where just like public.
3 . private - two leading underscore(__) are used to define members as private members
              they cannot be accessed outside the class. but by namemandling we can access it.

'''
#here is an example

class account:
    def __init__(self, ac_no, ac_name, ac_bal):
        self.acc_no = ac_no #public variable # accessed any where in the program
        self._acc_name = ac_name #protected variable # accesses in class and sub class
        self.__acc_bal = ac_bal #private variable _classname__var # accessed only in class and by taking classname.objectvariable
        
acc1 = account(123567839, 'Sreya', 10000)
print(acc1.acc_no) # 123567839
print(acc1._acc_name)#Sreya # protected and can be changed
acc1._acc_name = 'Sreya Gracy' # we are trying to modify and if its neccessary we need to modify
print(acc1._acc_name)
#print(acc1.__acc_bal)#attribute error it cannot be accessed the outside the class because it is private ...
#it can be access using some other name _classname__var,accessed only in class and by taking classname.objectvariable 
print(acc1._account__acc_bal)#10000
acc1._account__acc_bal = 20000#namemangling .. but not good programming practice
print(acc1._account__acc_bal)

# using object if we modify class attribute for that particular object
#only instance of class attribute will be created not for all the objects


#if namemangling .. but not good programming practice but can be possible using getter and setter methods
class account:
    def __init__(self, ac_no, ac_name, ac_bal):
        self.acc_no = ac_no #public variable # accessed any where in the program
        self._acc_name = ac_name #protected variable # accesses in class and sub class
        self.__acc_bal = ac_bal #private variable _classname__var # accessed only in class and by taking classname.objectvariable
    #getter method - used to retrieve the private variables
    #since private variable is accessed inside the class
    #we are defining function to access the private variable since its inside the class
        
    def balance_enquiry(self):
        print(f"current balance:{self.__acc_bal}")
    #setter method - used to update the privare variables
    def deposit(self, amount):
        if amount > 0:
            self.__acc_bal += amount
            print('amount deposited')
        else:
            print('no deposit')
            
        
        
acc1 = account(123567839, 'Sreya', 10000)
acc1.balance_enquiry()
acc1.deposit(1000)
acc1.balance_enquiry()

#encapsulation:
'''
it is the principle of budling the attribute and methods together as a
class and restricting the access to some of the components of the class
using access modifiers

'''







class Account:
    def __init__(self, ac_no, ac_name, ac_bal):
        self.acc_no = ac_no              # public
        self._acc_name = ac_name         # protected
        self.__acc_bal = ac_bal          # private

    # getter method
    def balance_enquiry(self):
        print(f"Current balance: {self.__acc_bal}")

    # setter method
    def deposit(self, amount):
        if amount > 0:
            self.__acc_bal += amount
            print("Amount deposited successfully.")
        else:
            print("Deposit amount must be greater than 0.")
            

# --- taking input from user ---
ac_no = int(input("Enter Account Number: "))
ac_name = input("Enter Account Holder Name: ")
ac_bal = float(input("Enter Initial Balance: "))

# create object using user input
acc1 = Account(ac_no, ac_name, ac_bal)

# show balance
acc1.balance_enquiry()

# deposit input
amt = float(input("Enter amount to deposit: "))
acc1.deposit(amt)

# show updated balance
acc1.balance_enquiry()






###
class Account:
    def __init__(self, ac_no, ac_name, ac_bal):
        self.acc_no = ac_no
        self._acc_name = ac_name
        self.__acc_bal = ac_bal

    # getter method using return
    def balance_enquiry(self):
        return self.__acc_bal #using return instead of print

    # setter method
    def deposit(self, amount):
        if amount > 0:
            self.__acc_bal += amount
            print("Amount deposited successfully.")
        else:
            print("Invalid amount.")

# taking user input
ac_no = int(input("Enter Account Number: "))
ac_name = input("Enter Account Holder Name: ")
ac_bal = float(input("Enter Initial Balance: "))

acc1 = Account(ac_no, ac_name, ac_bal)

# deposit
amt = float(input("Enter amount to deposit: "))
acc1.deposit(amt)

# print returned balance
print("Current balance:", acc1.balance_enquiry())

