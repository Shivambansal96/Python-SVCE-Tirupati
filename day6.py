# # # # # dict = {
# # # # #     "name" : "Shivam",
# # # # #     "isTrainer": True,
# # # # #     "marks" : {
# # # # #         'python' : 98,
# # # # #         "NOdeJS" : 90,
# # # # #         "C" : 99
# # # # #     }
# # # # # }

# # # # # # print(dict["marks"]['python'])

# # # # # # print(dict.keys())
# # # # # # print(dict.values())
# # # # # # print(dict.items())
# # # # # # print(dict.get("name"))
# # # # # # print(dict.get("naming"))
# # # # # # print("CODe ENds")
# # # # # # print(dict.update({'demo': 35}))
# # # # # # print(dict['demo'])

# # # # # # Q1

# # # # # myDict = {
# # # # #     'table' : ['a piece of furniture', 'lists of facts & figures'],
# # # # #     'cat' : 'a small animal'
# # # # # }

# # # # # print(myDict)

# # # # # Q2

# # # # # myDict = {}
# # # # # sub1 = input("Enter sub 1 = ")
# # # # # sub2 = input("Enter sub 2 = ")
# # # # # sub3 = input("Enter sub 3 = ")

# # # # # marks1 = int(input("Enter marks of sub1 = "))
# # # # # marks2 = int(input("Enter marks of sub2 = "))
# # # # # marks3 = int(input("Enter marks of sub3 = "))

# # # # # myDict.update({sub1: marks1})
# # # # # myDict.update({sub2: marks2})
# # # # # myDict.update({sub3: marks3})
# # # # # print(myDict)



# # # # # myDict = {}

# # # # # for i in range(3):
# # # # #     sub = input(f"Enter subject {i+1} = ")
# # # # #     marks = int(input(f"Enter marks of {sub} = "))
# # # # #     myDict.update({sub : marks})

# # # # # print(myDict)




# # # # # myDict = {}
# # # # # n = int(input("How many subjects do you have = "))

# # # # # for i in range(n):
# # # # #     sub = input(f"Enter subject {i+1} = ")
# # # # #     marks = int(input(f"Enter marks of {sub} = "))
# # # # #     # myDict.update({sub : marks})
# # # # #     myDict[sub] = marks
    

# # # # # print(myDict)



# # # # myDict = {
# # # #     'name': "Shivam",
# # # #     'marks' : 98
# # # # }
# # # # myDict.update({'name': "Bansal"})

# # # # print(myDict)

# # # # myDict = {}

# # # # for i in range(1, 11):
# # # #     myDict[i] = i ** 2

# # # # print(myDict)



# # # # myArr = [3, 2, 42, 2, 84, 42, 3, 3, 88, 9]
# # # # myArr = [10, 10, 10, 2, 2, 2, 2, 1]
# # # # myArr = [3, 2, 42, 2, 84, 42, 3, 3,  88, 9, 3]

# # # # countFreq = {}
# # # # for i in myArr:
# # # #     if i in countFreq:
# # # #         countFreq[i] += 1
# # # #     else:
# # # #         countFreq[i] = 1

# # # # print(countFreq)




# # # myArr = [3, 2, 42, 2, 84, 42, 3, 3,  88, 9, 3]
# # # countFreq = {}
# # # for i in range(len(myArr)):
# # #     count = 0
# # #     for j in range(len(myArr)):

# # #         if myArr[i] == myArr[j]:
# # #             count += 1
# # #     countFreq[myArr[i]] = count

# # # print(countFreq)
        



# # # def addition(a, b):
# # #     add = a + b

# # #     return add

# # # a = 5
# # # b = 10
# # # print(addition(a, b))




# # # def addition(a, b):
# # #     add = a + b

# # #     return add

# # # print(addition(5, 10))

# # # def addition(): # Definition / Parameter
# # #     a = 5
# # #     b = 10
# # #     add = a + b

# # #     return add

# # # print(addition()) # Calling / Arguments 


# # # def addition(): 
# # #     a = 5
# # #     b = 10
# # #     add = a + b

# # #     print(add)
    
# # # ans = addition()
# # # print(ans)


# # # def addition(a, b, c, d, e):
# # #     add = a + b + c + d + e

# # #     print(add)
    
# # # ans = addition(3, 4, 9, 7, 4)
# # # print(ans)


# # # def addition(x, y):
# # #     add = x + y
# # #     return add

# # # a = 5
# # # b = 10
# # # print(addition(a, b))


# # # def lengthOfArr(myArr):
# # #     return len(myArr)

# # # myArr = [84,8541,85415,6,61,64,61,61,984]
# # # print(lengthOfArr(myArr))


# # def lengthOfArr(myArr):
# #     for i in myArr:
# #         print(i, end= " ")

# # myArr = [84,8541,85415,6,61,64,61,61,984]
# # lengthOfArr(myArr)


# # def add(a, b):
# #     print(a + b)

# # add(2, 3)
# # add(50, 31)
# # add(5130, 32131)
# # add(13150, 3624621)
# # add(51350, 362461)
# # add(5064262, 364261)

# def factorial(n):
#     fact = 1

#     for i in range(1, n+1):
#         fact *= i

#     return fact

# n = 5
# r = 3

# a = factorial(n)
# b = factorial(n - r)
# c = factorial(r)

# permutation = a // b
# print(permutation)

# combination = a // b * c
# print(combination)

