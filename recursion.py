
"""def factorial(num):
    if num == 1:
        return 1
    else:
        return factorial(num - 1)*num

num = int(input("Enter a number: "))
print(factorial(num))
"""


"""def fibbo(num):
    if num == 1:
        return 0
    elif num ==2 or num == 3:
        return 1

    else:
        return fibbo(num-1)+fibbo(num-2) 

num = int(input("Enter a number: "))
print(fibbo(num))
"""


"""def fibbo(num):
    li = []

    num1 = 0
    num2 = 1

    for i in range(num):
        li.append(num1)

        num1,num2 = num2,num1+num2
    return li

num = int(input("Enter a number: "))

print(fibbo(num))"""


"""def palindrome(num):
    temp = num
    rev = 0

    while temp > 0:
        n = temp % 10
        rev = rev*10+n
        temp = temp // 10

    if num == rev:
        return "palindrome"
    else:
        return "not palindrome"

num = int(input("Enter a number: "))

print(palindrome(num))"""


"""class Employee:
    __companyName = "IndeGene"
    def __init__(self, name, salary, desg, gender, age):
        self.name = name
        self.salary = salary
        self.desg = desg
        self.gender = gender
        self.age = age

    def getCompany(self):
        return self.__companyName
    
    def setCompany(self, name):
        self.__companyName = name
    
emp1 = Employee("John", 20000, "Software Engineer", "Male", 25)

print(emp1.getCompany())

emp1.setCompany("TestYantra")
print(emp1.getCompany())"""


"""class grandParent:
    def grand_parent(self):
        print("grand parent")

class Parent(grandParent):
    def parent(self):
        print("parent")

class Child(Parent):
    def child(self):
        print("child")


obj1 = Child()
obj1.grand_parent()"""

# from time import sleep
"""def detonate(n):
    def decorator(func):
        def wrapper(*args):
            for i in range(n,0,-1):
                print(f"Explosion at {i} sec")
                sleep(1)
            func(*args)
        return wrapper
    return decorator

n = 5
@detonate(n)
def C4():
    print("BOOOOMMMMM...")

n = 10
@detonate(n)
def nukes():
    print("You are so fucked up...")

C4()
nukes()"""



"""class AgeLessError(Exception):
    ...

try:
    age = int(input("Enter your age: "))
    if age > 18:
        print("you can vote")
    else:
        raise AgeLessError
except AgeLessError:
    print("Age should be greater than 18")"""




def fibbo(num):
    if num == 1:
        return 0
    elif num == 2 or num == 3:
        return 1

    else:
        return fibbo(num-1)+fibbo(num-2)


num = int(input("Enter a number: "))

print(fibbo(num))





