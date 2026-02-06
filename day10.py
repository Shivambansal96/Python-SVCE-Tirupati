# # print(2 + 3)  # Arithmetic Operation
# # print("2" + "3") # Concatenate
# # print([2] + [3]) # Merge



# # a = "2i + 3"
# # b = "3i + 4"

# # print(a + b)


# # class ComplexNum:
# #     def __init__(self, real, img):
# #         self.real = real
# #         self.img = img

# #     def showDetails(self):
# #         print(f"{self.real}i + {self.img}")

    
# #     def __add__(self, c2):
# #         newRealNum = self.real + c2.real
# #         newImgNum = self.img + c2.img
# #         return ComplexNum(newRealNum, newImgNum)


# #     # def add(self, newNum):
# #     #     newRealNum = self.real + newNum.real
# #     #     newImgNum = self.img + newNum.img

# #     #     # return (f"{newRealNum}i + {newImgNum}")
# #     #     return ComplexNum(newRealNum, newImgNum)


# # c1 = ComplexNum(3, 8)
# # c2 = ComplexNum(2, 5)
# # c1.showDetails()
# # c2.showDetails()

# # # c3 = c1.add(c2)
# # c3 = c1 + c2
# # c3.showDetails()

    

# class ComplexNum:
#     def __init__(self, real, img):
#         self.real = real
#         self.img = img

#     def showDetails(self):
#         print(f"{self.real}i + {self.img}")

    
#     def __sub__(self, c2):
#         newRealNum = self.real - c2.real
#         newImgNum = self.img - c2.img
#         return ComplexNum(newRealNum, newImgNum)


#     # def add(self, newNum):
#     #     newRealNum = self.real + newNum.real
#     #     newImgNum = self.img + newNum.img

#     #     # return (f"{newRealNum}i + {newImgNum}")
#     #     return ComplexNum(newRealNum, newImgNum)


# c1 = ComplexNum(3, 8)
# c2 = ComplexNum(2, 5)
# c1.showDetails()
# c2.showDetails()

# # c3 = c1.sub(c2)
# c3 = c1 - c2
# c3.showDetails()

    
# # Stack Overflow
# def show(n):

#     print(n)
#     show(n - 1)

# show(10)

# # i = 10
# # while True:
# #     print(i)
# #     i -= 1


