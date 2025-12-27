# Day 2 - Variables and Built In Functions

firstName = "James"
surName = "Jark"
fullName = (firstName) + ' ' + (surName)
country = 'Iceland'
city = 'Iceland City'
age = 34
year = 2025
isMarried = False
isTrue = True
isLightOn = isTrue

# print(type(firstName))
# print(type(surName))
# print(type(fullName))
# print(type(country))
# print(type(city))
# print(type(age))
# print(type(year))
# print(type(isMarried))
# print(type(isTrue))
# print(type(isLightOn))

# fNameLen = len(firstName)
# sNameLen = len(surName)
# lenDiff = fNameLen - sNameLen
# print(lenDiff)

# num1 = 5
# num2 = 4
# totalNum = num1 + num2
# DifferenceNum = num1 - num2
# multNum = num1 * num2
# divNum = num1 / num2
# modNum = num1 % num2
# powerOfNum = num1 ** num2
# print(totalNum, DifferenceNum, multNum, divNum, modNum, powerOfNum) 

pi = 3.14
radius = input("What is the radius of the circle?: ")
radius = int(radius)
RSquared = radius ** 2
areaOfCircle = pi * RSquared
circumOfCircle = 2 * radius
print(areaOfCircle, circumOfCircle)