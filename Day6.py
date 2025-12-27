#Day6 - Tuples

brothers = ('Jmichael', 'Himilton')
sisters = ('Anna', 'Kylee')

siblings = brothers + sisters
print(siblings)
familyMembers = list(siblings)
familyMembers.insert(2, 'Pippy')
familyMembers.insert(5, 'Patty')
print(familyMembers)
print(len(familyMembers))

veggies = ('Aubergine', 'Carrot', 'Celery')
fruits = ('Nahna', 'Pomme', 'Blueberry')
anmalProd = ('Milk', 'Eggs', 'Yoghurt')

foodStuff = veggies + fruits + anmalProd
print(foodStuff)
midThree = foodStuff[3:6]
FrontThree = foodStuff[0:3]
BackThree = foodStuff[6:]
print(FrontThree)
print(midThree)
print(BackThree)
# del foodStuff
# print(foodStuff)

nordic = ('Denmark', 'Finland', 'Iceland', 'Norway', 'Sweden')
nordic.index('Estonia')
print(nordic.index('Iceland'))