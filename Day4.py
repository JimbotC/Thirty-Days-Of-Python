# Day 4 - Strings

# str1 = 'thirty'
# str2 = 'days'
# str3 = 'of'
# str4 = 'python'
# space  = ' '
# fullStr = str1 + space + str2 + space  + str3 + space + str4
# print(fullStr) 

company = 'Coding For All'
print(company)
print(len(company))
print(company.upper())
print(company.lower())
print(company.title())
print(company.capitalize())
print(company.swapcase())
noCoding = company[7:]
print(noCoding)
print(company.find('Coding'))
print(company.replace('Coding', 'Python'))
print(company.split())
techCom = 'Facebook,Google,Microsoft,Apple,IBM,Oracle,Amazon'
print(techCom.split(','))
firstCharacter = company[0]
print(firstCharacter)
tenthCharacter = company[10]
print(tenthCharacter)
seventhChar = company[7]
eleventhChar = company[11]
CompAbrv = firstCharacter + seventhChar + eleventhChar
print(CompAbrv)
print(company.index('C'))
print(company.index('F'))
print(company.rindex('l'))

sentence = 'You cannot end a sentence with because because because is a conjunction'
sentence = sentence.lower()
print(sentence.find('because'))
print(sentence.rindex('because'))
noBecause = sentence[0:31] + sentence[55:]
print(noBecause)
print(company.startswith('Coding'))
print(company.endswith('coding'))
spaceCompany = '  Coding For All  '
print(spaceCompany.index('C'))
print(spaceCompany.rindex('l'))
noSpace = spaceCompany[2:16]
print(noSpace)
Python30 = '30DaysOfPython'
thirtyPy = 'Thirty_Days_Of_Python'
print(Python30.isidentifier())
print(thirtyPy.isidentifier())

pyLib = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
results = '# '.join(pyLib)
print(results)

newLine = 'I am enjoying this challenge \nI just wonder what is next'
print(newLine)

descriptors = 'Name  \tAge \tCountry \tCity'
info = 'Asabeneh 250 \tFinland \tHelsinki'
print(descriptors)
print(info)

radius = 10
area = 3.14 * radius ** 2
formatString = 'The Area of the circle with a radius of {} is {} '.format(str(radius), str(area))
print(formatString)

a = 8
b = 6
print('{} + {} = {}'.format(a, b, a + b))
print('{} + {} = {}'.format(a, b, a - b))
print('{} + {} = {}'.format(a, b, a * b))
print('{} + {} = {}'.format(a, b, a / b))
print('{} + {} = {}'.format(a, b, a % b))
print('{} + {} = {}'.format(a, b, a // b))
print('{} + {} = {}'.format(a, b, a ** b))