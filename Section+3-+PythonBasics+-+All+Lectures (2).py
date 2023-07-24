######## 1. print function###########
from re import A

print("hello rahul")
print("what is your name")
print(5)

######## 2. variable function###########
course = "how do you like the course"
print("course")
print(course)
course = 55
print(course)

######## 3 and 4. Data type - Integer, Float and Methods###########

integertest = 33
floattest = 33.5
print(type(integertest))
print(type(floattest))

# c = numbers.real
# k = decimal.real
#listtest  = [1,2,3]
# m = listtest.insert()


############ 5. Loops - for #########
data = 1, 2, 3, 4, 5
for k in data:
    print(k)

############6. Print variables in Strings---- ‘format()’ method
grade = '4th grade'
section = 'A'
print("My class is {} and section is {}".format(grade, section))

############ 7. Dictionary, Nested Dictionary#########

Dict = {1: 'Python', 2: 'For', 3: 'Lambda'}
for d in Dict.items():
    print(d)

for d in Dict.values():
    print(d)

element = Dict[1]
print("Value of element is {}".format(element))

####Nested Dictionary

nesteddictionary = {1: 'Python', 2: {'books': 'cloud', 'aws': 'Lambda'}}
print(nesteddictionary[2])
print(nesteddictionary[2]['books'])

### Loops and Dictionary Methods

for k in nesteddictionary.values():
    print(k)

for k in nesteddictionary.keys():
    print(k)
#######8 user input

name = input('Please enter your name')
grade = input('Please enter your grade')
print('My name is {} and my grade is {}'.format(name, grade))


##### 9 String Slicing
data = 'ASTRING'
print(data[2:4:1])

for a in data:
    print(a)


# A simple Python function to check
# whether x is even or odd


def evenOdd(x):
    if (x % 2 == 0):
        print("even")
    else:
        print("odd")


# Driver code to call the function
evenOdd(2)
evenOdd(3)


def square_value(num):
    """This function returns the square
    value of the entered number"""
    return num ** 2

print(square_value(2))
print(square_value(-4))