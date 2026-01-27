# # print("My name is ", "Shivam", sep="= ")

# # # a = 5
# # # b = 5
# # # sumValue = a + b
# # # print(sumValue)




# # # a = 4
# # # a += 1
# # # print(a)

# # a = 3 
# # b = "3"
# # b = int(b)
# # print(a+ b)
# # print(type(a))


# name = input("Enter your name = ")
# age = int(input("Enter your age = "))
# city = input("Enter your city: ")

# # print("Hello ", name, ", you are ", age, " years old and live in ", city, sep="")

# print(f"Hello {name}, you are {age} years old and live in {city}.")


# # Practice Set 2
# # Q1

# a = int(input("Enter a number = "))
# b = int(input("Enter another number = "))

# sumValue = a + b

# print(f"The sum of {a} and {b} = {sumValue}")


# Q2 
# side = int(input("Enter a side = "))

# area = side * side
# area = side ** 2  # Exponent
# print(f"Area of a square = {area}")

# # Q3

# num1 = float(input("Enter a number = "))
# num2 = float(input("Enter another number = "))

# avg = (num1 + num2) // 2

# print(f"Average of {num1} and {num2} = {avg}")


# # Q4

# a = int(input("Enter a number = "))
# b = int(input("Enter another number = "))

# print(a>=b)



# name = "Shivam"

# a = name[::-1]

# print(a)


# name = "Shivam"

# print(name[0] == name[-1])
# print(name[0] == name[len(name)-1])




fruit = "aPple"

print(fruit.capitalize())
print(fruit.count('p'))
print(fruit.endswith('e'))
print(fruit.find('z'))
print(fruit.index('p'))
print(fruit.replace('p', 'c', 1))
print(fruit.swapcase())
print(fruit.upper())
print(fruit)