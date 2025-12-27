##Day 9 - Conditionals

def practice():
    ##If statements
    a = 3
    if a > 0:
        print("A is a positive number")
    else:
        print("A is a negative number")
     
    ##Else If statements   
    b = 0
    if b > 0:
        print("B is a positive number")
    elif b < 0:
        print("B is a negative number")
    else:
        print("B is zero")
        
    ##Shorthand
    c = 3
    print("C is positive") if c > 0 else print("C is negative")
    
    ##Nested
    d = 2
    if d > 0:
        if d % 2 == 0:
            print("D is a positive and even integer")
    elif d == 0:
        print('D is zero')
    else:
        print("D is negative")
        
    ##Condition Statements
    e = 3
    if e > 0 and e % 2 == 0:
        print("E is positive and even")
    elif e > 0 and e % 2 != 0:
        print("E is positive and odd")
    else:
        print("E is either 0 or negative")
    
    
    user = 'James'
    accessLevel = 3
    if user == 'admin' or accessLevel >= 4:
        print("Access Granted!")
    else:
        print("Access Denied!")
       
def exercise():
    print("Age Verification")
    age = int(input("Please enter your age: "))
    if age >= 18:
        print("You are old enough to learn how to drive")
    else:
        print("You need", 18-age, "more years to learn to drive")
    print("-----------")
       
    print("Age Comparer") 
    myAge = 23
    yourAge = int(input("Please enter you age: "))
    if myAge > yourAge:
        print("I am older than you by:", myAge - yourAge, "years")
    elif myAge == yourAge:
        print("We are the same age")
    else:
        print("You are older than me by:", yourAge - myAge, "years")
    print("-----------")
    
    print("Number Comparer")
    intA = int(input("Please enter a value for A: "))
    intB = int(input("Please enter a value for B: "))
    if intA > intB:
        print(intA , "is greater than", intB)
    elif intA == intB:
        print(intA , "is equal to", intB)
    else:
        print(intB, "is greater than", intA)
    print("-----------")
    
    print("Auto Grader")
    score = int(input("Please enter the score the student achieved: "))
    if score <= 100 and score >= 91:
        print("A")     
    elif score <= 90 and score >= 71:
        print("B") 
    elif score <= 70 and score >= 61:
        print("C")
    elif score <= 60 and score >= 50:
        print("D") 
    elif score < 50 and score >= 0:
        print("F")  
    else:
        print("Invalid score results")
    print("-----------")
    
    
    
#practice()
exercise()