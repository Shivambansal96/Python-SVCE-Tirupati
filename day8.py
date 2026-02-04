# # # class Student:
# # #     name = "Shivam Bansal"

# # #     def hello(self):
# # #         print(f"Hello {self.name}")

# # # s1 = Student()
# # # print(s1.name)
# # # # s1.hello()

# # # s2 = Student()
# # # print(s2.name)



# # # class Student:
# # #     name = "Shivam"

# # #     def __init__(self):
# # #         print(f"Constructor = {self}")
# # #         print("Student object is created.")

# # # s1 = Student()            # Constructor
# # # print(f"OUTSIDE = {s1}")
# # # print(s1.name)

# # # s2 = Student()
# # # print(s2.name)






# # # class Student:

# # #     def __init__(self, fullName):
# # #         self.name = fullName

# # #     def welcomeMsg(self):
# # #         print(f"Welcome {self.name}")

# # # s1 = Student("Shiv")            # Constructor
# # # s1.welcomeMsg()
# # # # print(s1.name)

# # # s2 = Student("Shivam")          # Constructor
# # # s2.welcomeMsg()
# # # # print(s2.name)







# # # class Student:
# # #     fN = "demo Person"

# # #     def __init__(self, fullName="anonymous"):
# # #         self.name = fullName

# # #     def welcomeMsg(self):
# # #         print(f"Welcome {self.name}")

# # # s1 = Student("Shiv")            # Constructor
# # # s2 = Student("Shivam")          # Constructor

# # # s1.welcomeMsg()
# # # s2.welcomeMsg()

# # # s3 = Student()
# # # print(s3.fN)


# # class Student:
# #     marks = 24

# # s1 = Student()
# # # del s1.marks
# # # del s1
# # print(s1.marks)


# class Student:

#     def __init__(self, name, sub1, sub2, sub3):
#         self.name = name
#         self.sub1 = sub1
#         self.sub2 = sub2
#         self.sub3 = sub3
    
#     def avg(self):
#         sumOfAll = self.sub1 + self.sub2 + self.sub3
#         avgOf3 = sumOfAll // 3
#         print(f"{self.name}'s Average = {avgOf3}")


# s1 = Student("Shivam", 96, 98, 100)
# s2 = Student("Shiv", 100, 100, 100)
# s3 = Student("Shiva", 99, 99, 99)
# s4 = Student("Mohini", 9, 19, 19)
# s5 = Student("Anita", 99, 59, 69)

# s1.avg()
# s2.avg()
# s3.avg()
# s4.avg()
# s5.avg()
        


class Circle:
    def __init__(self, radius):
        self.r = radius

    def areaOfCircle(self):
        area = (22/7) * self.r * self.r
        area= int(area)
        print(f"Area of a Circle with radius {self.r} = {area}")

    def perimeterOfCircle(self):
        perimeter = 2 * (22/7) * self.r
        perimeter = int(perimeter)
        print(f"Perimeter of a Circle with radius {self.r} = {perimeter}")

    @staticmethod
    def testingStaticMethod():
        print("Wasting my time!!!")

c1 = Circle(5)
c1.areaOfCircle()
c1.perimeterOfCircle()
c1.testingStaticMethod()