# # # # # vehicle_type= int(input())
# # # # # hours= int(input())
# # # # # weekend= int(input())
# # # # # fare = 0
 
# # # # # if vehicle_type == 2:
# # # # #     fare= 20
# # # # #     if hours > 2:
# # # # #         fare += (hours-2) * 20
# # # # # elif  vehicle_type == 4:
# # # # #     fare= 40
# # # # #     if hours > 2:
# # # # #         fare += (hours-2) * 20


# # # # age =int(input())
# # # # freq =int(input())
# # # # interest_pt =int(input())
# # # # base_fee = 0
# # # # category = ""
# # # # plan_name= ""
# # # # PT= 700
# # # # if age < 18:
# # # #     base_fee = 800
# # # #     category = "Junior"
# # # # elif 18<= age <60:
# # # #     base_fee= 1200
# # # #     category = "Adult"
# # # # else: 
# # # #     base_fee= 900
# # # #     category = "Senior"

# # # # if freq <= 2:
# # # #     plan_name = "Casual"
# # # # elif 2<freq<= 4:
# # # #     base_fee+=300
# # # #     plan_name = "Regular"
# # # # elif 4< freq<=7:
# # # #     base_fee= 500
# # # #     plan_name = "Intense"

# # # # if interest_pt == 1 and category != "Junior":
# # # #     base_fee += PT
# # # #     print(f"{category} {plan_name} + PT")
# # # # elif interest_pt == 0 or category == "Junior":
# # # #     print(f"{category} {plan_name}")

# # # # print(base_fee)


# # # # # # Linear Search

# # # # myArr = [1, 4, 9, 16, 42, 31, 5, 7, 3, 6]
# # # # target = int(input("Enter the number you want to search = "))


# # # # if target in myArr:
# # # #     print(f"Target Found at index {myArr.index(target)}")
# # # #     # print(f"Target Found")
# # # # else:
# # # #     print("Target not Found")





# # # myArr = [1, 4, 9, 16, 42, 31, 4, 7, 3, 6]
# # # target = int(input("Enter the number you want to search = "))


# # # for i in range(len(myArr)):
# # #     if target == myArr[i]:
# # #         print(f"Target Found at index {i}")

# # # else:
# # #     print("Target not Found !!!")



# # # a = (3,)

# # # print(type(a))


# # # a = (4, 63, 2, 3, 56, 78, 9, 3)

# # # a.count(4)
# # # a.index(3)


# # # tup = ("C", "D", "A", "A", "B", "B", "A")

# # # newList = list(tup)
# # # newList.sort()

# # # print(newList)


# # tup = (43, 45, 42, 67, 8, 9, 99, 53, 42)

# # for i in tup:
# #     print(i, end=" ")
# # print()


# # countOdd = 0
# # countEven = 0

# # for i in range(len(tup)):
# #     if tup[i] % 2 == 0:
# #         countEven += 1
# #     else:
# #         countOdd += 1

# # print(f"There are {countEven} EVEN elements")
# # print(f"There are {countOdd} ODD elements")



# # favMovies = []

# # a = input("Enter movie 1 = ")
# # b = input("Enter movie 2 = ")
# # c = input("Enter movie 3 = ")

# # favMovies.append(a)
# # favMovies.append(b)
# # favMovies.append(c)

# # print(favMovies)



# # favMovies.append(a)
# # favMovies.append(b)
# # favMovies.append(c)

# # print(favMovies)



# # favMovies = []

# # for i in range(3):
# #     a = input(f"Enter movie {i+1} = ")
# #     favMovies.append(a)

# # print(favMovies)



# # a, b, c, d = map(str, input("abc = ").split(" "))

# # print(d)


# # myArr = list(map(int, input("abc = ").split("-")))

# # print(myArr)


# # a = set()

# # print(type(a))



# # techStacks = { "C", "Java", "Python", "C", "Java", "C++", "PHP"}

# # print(f"Total classes required: {len(techStacks)}")

# text1 = "Python is a great programming language".lower()
# text2 = "Many developers love the python language".lower()

# setA = set(text1.split())
# setB = set(text2.split())

# commonWords = setA.intersection(setB)
# allWords = setA.union(setB)

# print(commonWords)
# print(len(allWords))



# myArr = [3, 5, 7, 3, 9, 5, 3, 9]

# duplicates = []
# for i in myArr:
#     if myArr.count(i) >= 2 and i not in duplicates:
#         duplicates.append(i)

# print(duplicates)



# myArr = [3, 5, 7, 3, 9, 5, 3, 9]

# setA = set()
# for i in range(len(myArr)):
#     for j in range(i+1, len(myArr)):
#         if (myArr[i] == myArr[j]):
#             setA.add(myArr[i])

#         print(setA)





myArr = [3, 5, 7, 3, 9, 5, 3, 9]

setA = set()
for i in range(len(myArr)):
    count = 0
    for j in range(len(myArr)):
        if (myArr[i] == myArr[j]):
            count += 1

    if count == 2:
        setA.add(myArr[i])

print(setA)