# myArr = [3, 4, 24, 56, 4, 1, 77, 87]
# target = 80
# indexesList = []

# for i in range(len(myArr)):
#     for j in range(i+1, len(myArr)):
        
#         if myArr[i] + myArr[j] == target:
#             indexesList.append((myArr[i], myArr[j]))

# if len(indexesList) != 0:
#     for i in indexesList:
#         print(f"Target found at indexes {i}")
# else:
#     print("Target not Found!!!")




# myArr = [5, 3, 1, 2, 5, 5, 1, 2]
# newList = []

# for i in range(len(myArr)):
#     for j in range(len(myArr)):

#         if myArr[i] == myArr[j] and myArr[i] not in newList:
#             newList.append(myArr[i])

# print(newList)




# PATTERNS


# for i in range(5):
#     for j in range(5):
#         print("*", end=" ")
#     print()


# n = 5
# for i in range(n):
#     for j in range(i+1):
#         print("*", end=" ")
#     print()



# n = 5
# for i in range(n):
#     for j in range(i+1):
#         print(j+1, end=" ")
#     print()

# n = 5
# for i in range(n):
#     for j in range(i+1):
#         print(i+1, end=" ")
#     print()

# n = 5
# start = 65
# for rows in range(start, start+n):
#     for cols in range(start, rows+1):
#         print(chr(rows), end=" ")
#     print()



# n = 5

# for i in range(n):
#     for j in range(i, n):
#         print("*", end=" ")
#     print()



# n = 5

# for i in range(n):
#     for j in range(n-i):
#         print("*", end=" ")
#     print()


n = 5

for i in range(n):
    for spaces in range(n - i - 1):
        print(" ", end=" ")

    for stars in range(i+1):
        print(i+1, end="   ")

    print()