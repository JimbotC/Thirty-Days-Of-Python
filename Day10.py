##Day 10 - Loops

def practice():
    print("--While Loops--")
    count = 0
    while count < 5:
        print(count)
        count += 1
    else:
        print(count)
    
    while count < 5:
        print(count)
        count += 1
        if count == 3:
            break
        
    while count < 5:
        if count == 3:
            count += 1
            continue
        print(count)
        count += 1
        
    print("--For Loops--")
    ##List
    iNumbers = [1, 2, 3, 4, 5]
    for inumber in iNumbers:
        print(inumber)
    
    ##String
    language = 'Python'
    for letter in language:
        print(letter)
    print("-")
        
    for i in range(len(language)):
        print(language[i])
        
    ##Tuple
    tNumbers = (0, 1, 2, 3, 4, 5)
    for tnumber in tNumbers:
        print(tnumber)
        
    ##Dictonary
    person = {
        'firstName': 'Garry',
        'lastName': 'Hanna',
        'age': 250,
        'country': 'USA',
        'isMarred': True,
        'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
        'address':{
            'city': 'New Jersey',
            'street': 'Space street',
            'zipcode': '02210'
        }
    }
    for key in person:
        print(key)
    
    print("----------")
        
    for key, Value in person.items():
        print(key, Value)
        
    ##Set
    itCompanies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
    for company in itCompanies:
        print(company)
    
    print("--Break and Continues--")
    ##Break
    numbers = (0, 1, 2, 3, 4, 5)
    for number in numbers:
        print(number)
        if number == 3:
            break
    
    ##Continue
    for number in numbers:
        print(number)
        if numbers == 3:
            continue
        print('Next number should be ', number + 1) if number != 5 else print("Loop's end")
    print("Outside of loop")
    
    print("--Range Function--")
    for number in range(11):
        print(number + 1)
        
    print("--Nested Loops--")
    jojos = {
        'firstName': 'Jotaro',
        'lastName': 'Kujo',
        'age': 40,
        'country': 'Japan', 
        'isMarried': False,
        'parts': ['Part 3', 'Part 4', 'Part 6']
    }
    for key in jojos:
        if key == 'parts':
            for part in jojos['parts']:
                print(part)
    
def exercise():
    ##Ex 1
    i = 0
    for i in range(11):
        print(i)
        
    while i > 10:
        print(i)
        i += 1
    
    j = 10
    negative = (10, 9, 8, 7, 6, 5, 4, 3, 2, 1,0)
    for k in negative:
        print(k)
        
    while j != 0:
        print(j)
        j -= 1
    print(j)
    
    prints = (print("#"), print("##"), print("###"), print("####"), print("#####"), print("######"), print("#######"))
    for i in prints:
        prints
        
    squared = 0
    total = 0
    while total < 100:
        total = squared ** 2
        print(squared, "x", squared, "=", total)
        squared += 1
        
    coding = ("Python", "Numpy", "Pandas", "Django", "Flask")
    for code in coding:
        print(code)
    
    oddEven = 0
    for oddEven in range(101):
        if oddEven % 2 == 0:
            print(oddEven)
    
    for oddEven in range(101):
        if oddEven % 2 != 0:
            print(oddEven)
    
    ##Ex2
    add100 = 0
    for i in range(100 + 1):
        add100 = add100 + i
    print("The sum of all numbers is", add100)
    
    addOddEven = 0
    addOdd = 0
    addEven = 0
    for addOddEven in range(100 + 1):
        if addOddEven % 2 == 0:
            addEven += addOddEven
        else:
            addOdd += addOddEven
    print("The sum of all evens is " + str(addEven) + ".", "The sum of all odd is", addOdd)
    
    ##Ex3
    fruit = ['banana', 'orange', 'mango', 'lemon']
    ##For Loop
    reversedFruit = []
    for i in range(len(fruit) -1, -1, -1):
        reversedFruit.append(fruit[i])
    print(reversedFruit)
    
    ##While Loop
    revFruit = []
    end = len(fruit) - 1
    while end >= 0:
        revFruit.append(fruit[end])
        end -= 1
    print(revFruit)
        
practice()
exercise()