##Day 8 - Dictionaries

def practice():
    emptyDict = {}
    diction = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}

    person = {
        'firstName': 'James',
        'lastName': 'Michael',
        'age': 23,
        'country': 'UK',
        'isMarried': False,
        'skills': ['Python', 'MongoDB', 'JavaScript'],
        'address': {
            'street': 'London Town',
            'postCode': 'E12 5PS'
        }
    }
    print(len(person))
    print(person['firstName'])
    print(person['lastName'])
    print(person['country'])
    print(person['isMarried'])
    print(person['skills'])
    print(person['skills'][0])
    print(person['address']['postCode'])
    ##print(person['city']) Throws up an error because it does not exist therefore when using the .get function on a key that does not exist it returns 'None'.
    print(person.get('city'))

    ##Adding to a dictionary
    person['jobTitle'] = 'Yog Miner'
    person['skills'].append('HTML')
    #print(person)

    ##Modifying
    person['firstName'] = 'Semaj'
    person['age'] = 55
    print(person)

    ##Checking keys
    print('skills' in person)
    print('jobTitle' in person)
    print('Gender' in person)

    ##Removing from a dictionary
    ##pop(key) - will remove the item with the specified key name
    ##popitem() - removes the last item
    ##del[''] - removes an item with the specified key name
    person.pop('firstName')
    #print(person)
    person.popitem()
    #print(person)
    del person['isMarried']
    print(person)
    
    ##Changing to a list of items
    #print(person.items())
    ##This changes the dictionary into a list of tuples
    
    ##Clearing a dictionary
    #print(person.clear())
    
    ##Deleting a dictionary
    #del person
    
    ##Copying a dictionary
    personCopy = person.copy()
    #print(personCopy)
    
    ##Getting dictionary values as a list
    values = person.values()
    #print(values)

def excercise():
    dog = {
        'dogName': 'Ruben',
        'dogColour': 'White',
        'dogBreed': 'Morkie (derogatary)',
        'legAmount': 4,
        'age': 13
    }
    
    student = {
        'firstName': 'Geghard',
        'lastName': 'Yeva',
        'gender': 'Female',
        'age': 67,
        'maritalStatus': False,
        'skills': ['Analytical Skills', 'Legal Research', 'Cutural Awareness', 'Objective Analyis'],
        'address': {
            'country': 'Armenia',
            'city': 'Yerevan',
            'street': '0018, 36g Tigran Metsi Ave., #31'
        }
    }
    
    print(len(student))
    print('skills' in student)
    student['skills'].append('Lawman')
    student['skills'].append('DEA')
    keys = student.keys()
    print(keys)
    values = student.values()
    print(values)
    items = student.items()
    print(items)
    student.pop('age')
    del student
    
    
#practice()
excercise()