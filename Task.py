
number = 5#global scope/global namespace
def x (): #function of x
    number = 3 #local scope/local namespace
    print(number)
x() #call the function
print(number) #print the global variable


#example of indentation,Assignment:
x=10
if x > 0:
    print("true")# there we use 4 spaces its called indentation
else:
    print("false")

#Statements:
y=5 #Assignment statement
print(y)#Function call statement

#Example to chek validity of string

import keyword

M = "if"

if keyword.iskeyword(M):#keword module gives this iskeyword function
    print("M is a Python keyword.")
else:
    print("M is not a Python keyword.")

#Example of assign variables and other language
#in python
name = "Intizar"
age = 45
"""in other language
int age = 30; #in c++/java"""


#Example of To print a newline
print("MY ", end="")
print("name ", end="")
print("is ", end="")
print("Rimsha. ", end="")
print()
#basic calculator
def sum():
    j = int(input("Enter 1st number"))
    k = int(input("Enter 2nd number"))
    return j+k
def mul():
    j = int(input("Enter 1st number"))
    k = int(input("Enter 2nd number"))
    return j*k

def div():
    j = int(input("Enter 1st number"))
    k = int(input("Enter 2nd number"))
    return j/k

def sub():
    j = int(input("Enter 1st number"))
    k = int(input("Enter 2nd number"))
    return j-k

print("Enter 1(sum)/2(mul)/3(div)/4(sub)")
i =int(input("select: "))
if i==1:
    print(sum())
elif i==2:
    print(mul())
elif i==3:
    print(div())
elif i==4:
    print(sub())
else:
    print("Invalid slection")

