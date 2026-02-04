# # # # # # # # RECURSION
# # # # # # def show(n):

# # # # # #     if n == 0:
# # # # # #         return
    
# # # # # #     print(n)
# # # # # #     # print(f"Start Value inside the Function = {n}")
# # # # # #     show(n - 1)
# # # # # #     # print(f"End Value inside the Function = {n}")
    
# # # # # # n = 3
# # # # # # # print(f"Start Value OUTSIDE the Function = {n}")
# # # # # # show(n)
# # # # # # # print(f"End Value OUTSIDE the Function = {n}")


# # # # # def show(n):

# # # # #     if n == 11:
# # # # #         return
    
# # # # #     print(n)
# # # # #     show(n + 1)

# # # # # n = 1
# # # # # show(n)




# # # # def addSum(n):

# # # #     if n == 0:
# # # #         return
    
# # # #     return n + addSum(n - 1)

# # # # n = 10
# # # # addSum(n)



# # # # File HANDLING


# # # import os

# # # # a = open("demo.txt")
# # # # # a = open("demo.txt", "r")
# # # # # a = open("demo.txt", "w")


# # # # data = a.read()
# # # # # data = a.readline(13)
# # # # ChangeEle = a.write("I am Creating a new File")
# # # # # print(ChangeEle)
# # # # a.close()


# # # # b = open("demo.txt")
# # # # data = b.read()
# # # # b.close()
# # # # print(data)


# # # # c = open("demo.txt", "a")

# # # # data = c.write("\nI am adding a new Line")
# # # # print(data)


# # # # os.rename("demo.txt", "sample.txt")
# # # # os.remove("sample.txt")

# # # # -------------------------------- #

# # # # # Create a new File and write some content in it
# # # # newFile = open("practice.txt", "w")
# # # # newFile.write("Hi everyone.\nWe are learning File Handling I/O\nusing python\nI like programming in python.")
# # # # newFile.close()

# # # # Open the file, reading it and store the content in a variable
# # # sameFile = open("practice.txt", "r")
# # # data = sameFile.read()

# # # newData = data.replace("python", "javascript")

# # # # Open the file again to make changes in the file
# # # newFile = open("practice.txt", "w")
# # # newFile.write(newData)

# # # # print(newData)



# # # # # LAMBDA FUNCTION

# # # def addSum(a, b):
# # #     print(a + b)

# # # addSum(4, 5)

# # # a = lambda x, y: print(x + y)
# # # a(3, 4)

# # # a = lambda x: print(x**2)
# # # a(3)


# # # arr = [1, 2, 3, 4, 5]
# # # res = list(map(lambda x : x * 2, arr))

# # # print(res)


# # # # Print the perfect squares of n natural numbers and store it in a set.
# # # n = 10

# # # prefectSquares = set(map(lambda a:a**2, range(1, n+1)))

# # # print(prefectSquares)

# # # ERROR HANDLING

# # # try:
# # #     a = int(input())
# # #     b = int(input())

# # #     print(a / b)

# # # except:
# # #     print("Invalid Input")


# # # try:
# # #     a = int(input())
# # #     b = int(input())

# # #     print(a / b)

# # # except Exception as a:
# # #     print("ERROR = ", a)

# # # print("CODE ENDS")


# # # try:
# # #     a = int(input())
# # #     b = int(input())
# # #     # print(a / b)
# # #     print(a / b * c)

# # # except ZeroDivisionError:
# # #     print("Number cannot be divided 0")

# # # except NameError:
# # #     print("No variable found")

# # # print("CODE ENDS")



# # # try:
# # #     a = 5
# # #     b = 0
# # #     # c = a/b
# # #     print("TRY is working")

# # # except:
# # #     print("Except is working")

# # # finally:
# # #     print("I will work, i am not stupid like you.")


# # age = 19

# # if age >= 18 or age < 60:
# #     raise NameError("Age value not found")



# # # # miniProject - Random Password Generator

# import string
# import random

# # a = string.ascii_letters         # required
# # a = string.digits                # optional
# # a = string.punctuation
# a = string.printable             # VVIP
# # a = string.hexdigits
# # a = string.octdigits
# # a = string.whitespace

# randomPass = ""
# for i in range(5):
#     randomCharacter = random.choice(a)
#     randomPass += randomCharacter

# print(randomPass)
