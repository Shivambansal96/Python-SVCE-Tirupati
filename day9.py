# # # # # # # # class Student:

# # # # # # # #     name = "Shivam"

# # # # # # # #     def __init__(self, fullName="anonymous"):
# # # # # # # #         self.fullName = fullName


# # # # # # # # s1 = Student()
# # # # # # # # s2 = Student()
# # # # # # # # s3 = Student()

# # # # # # # # del s1
# # # # # # # # # print(s1.name)
# # # # # # # # print(s2.name)
# # # # # # # # print(s3.name)



# # # # # # # class Student:

# # # # # # #     name = "anonymous"

# # # # # # #     def __init__(self):
# # # # # # #         pass

# # # # # # #     @classmethod
# # # # # # #     def helloStudent(cls, name):
# # # # # # #         cls.name = name
# # # # # # #         print(cls.name)

# # # # # # # s1 = Student()
# # # # # # # s1.helloStudent("Shivam")

# # # # # # # # print(s1.name)



# # # # # # class Student:

# # # # # #     def __init__(self, m1, m2, m3):
# # # # # #         self.m1 = m1
# # # # # #         self.m2 = m2
# # # # # #         self.m3 = m3

# # # # # #     # @property
# # # # # #     def avgMethod(self):
# # # # # #         avg = (self.m1 + self.m2 + self.m3) // 3
# # # # # #         print(avg)

# # # # # # s1 = Student(10, 20, 30)
# # # # # # s1.avgMethod()

# # # # # # s1.m1 = 25

# # # # # # print(f"Marks = {s1.m1}")
# # # # # # s1.avgMethod()




# # # # # class Account:

# # # # #     def __init__(self, accNo, accPass):
# # # # #         self.accNo = accNo
# # # # #         self.__accPass = accPass

# # # # #     def __showPassword(self):
# # # # #         print(f"Password = {self.__accPass}")

# # # # #     def resetPassword(self, newPassword):
# # # # #         self.__showPassword()
# # # # #         self.__accPass = newPassword
# # # # #         self.__showPassword()
# # # # #         print("Password Reset Successfully !")

    
# # # # # a1 = Account(14380100115559, "Shivam@123")
# # # # # print(a1.accNo)
# # # # # # print(a1.__accPass)
# # # # # # a1.__showPassword()
# # # # # a1.resetPassword("Shivam@321")


# # # # # class Animal:

# # # # #     whoAreYou = "Animal"
# # # # #     def intro(self):
# # # # #         print("I am an Animal Class")

# # # # # class Carnivores(Animal):
# # # # #     a = 8

# # # # # class Lion(Carnivores):
# # # # #     b = 9

# # # # # a1 = Animal()
# # # # # c1 = Carnivores()
# # # # # l1 = Lion()

# # # # # l1.intro()


# # # # # class Animal:
# # # # #     name = "Animal"

# # # # # class Herbivores(Animal):
# # # # #     name = "Horses"

# # # # # class Omnivores(Animal):
# # # # #     name = "Humans"

# # # # # class Cow(Herbivores):
# # # # #     Gives = "Milk"


# # # # class Father:
# # # #     a = 4

# # # # class Mother:
# # # #     b = 1

# # # # class StupidSon(Father, Mother):
# # # #     c = 1


# # # # class A:
# # # #     a = 7

# # # #     def __init__(self):
# # # #         print("Class A")

# # # #     @staticmethod
# # # #     def Hello():
# # # #         print("Hello World")


# # # # class B(A):

# # # #     def __init__(self):
# # # #         print("Class B")
    
# # # #     def show(self):
# # # #         super().__init__()
# # # #         print(f"New Function Ends")
    
# # # # c1 = B()
# # # # # c1.show()



# # # class Employee:

# # #     def __init__(self):
# # #         self.role = input("Enter your role = ")
# # #         self.dept = input("Enter your Department = ")
# # #         self.salary = int(input("Enter your Salary = "))
# # #         print()

# # #     def showDetails(self):
# # #         print(f"Role = {self.role}")
# # #         print(f"Department = {self.dept}")
# # #         print(f"Salary = Rs {self.salary}")
# # #         print()

# # # # e1 = Employee()
# # # # e1.showDetails()

# # # class Engineer(Employee):

# # #     def __init__(self):
# # #         self.name = input("Enter your Name = ")
# # #         self.age = int(input("Enter your Age = "))
# # #         super().__init__()

# # #     def showDetails(self):
# # #         print(f"Name = {self.name}")
# # #         print(f"Age = {self.age}")
# # #         super().showDetails()

# # # eng1 = Engineer()
# # # eng1.showDetails()



# # from abc import ABC, abstractmethod

# # class Animal(ABC):

# #     @abstractmethod
# #     def legs():
# #         print("Animals can walk on 4 legs")

# # class Dog(Animal):

# #     def legs(self):
# #         print("Dogs can walk on 4 legs")

# # # a1 = Animal()
# # # a1.legs()

# # d1 = Dog()
# # d1.legs()


# class Account:

#     def __init__(self, name, bal):
#         self.name = name
#         self.balance = bal

#     def debit(self, amount):
#         if amount > self.balance:
#             print("Insufficient Amount")
#         else:
#             self.balance -= amount
#             print(f"Amount Debited = Rs {amount}")

#     def credit(self, amount):
#         self.balance += amount
#         print(f"Amount Credited = Rs {amount}")

#     def showBalance(self):
#         print(f"Balance = {self.balance}")

# a1 = Account("Shivam", 5)
# a1.debit(10)
# a1.credit(500)
# a1.showBalance()

 
