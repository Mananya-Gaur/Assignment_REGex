def greet():
    print("Hello, world!")

greet()
##factorial using function
def factorial(n):
    fact=1
    for i in range(1,n+1):
        fact= fact*i
    return fact

fact_of_5=factorial(5)
fact_of_10=factorial(10)

print(fact_of_10)
print(fact_of_5)

##take n numbers of innput and print table
def table(n):
    for i in range(1,10):
        print(n*i)

table(5)

##"from python functions import factorial"--> used to import a fuctions in the other file

##make afunction to return a list in whiv=ch there are 3 elements

def lst():
    s=[]
    for i in range(0,3):
        a=input("enter a element")
        s.append(a)
    return s
info=s
print(info)
lst()

##take a input true when all letters are in capital otherwise false

a=input("enter a string")
def cap(a):
    if a.isupper():
        return True
    else:
        return False

##or
def cap(string):
    return string.isupper()

cap('mam')

##Return a number which will be the sum of ACSII value of the input strings

def asc(string):
    num=0
    for i in string:
        num += ord(i)
    return num
    # print(num)

q=asc('mananya')
print(q)

##or
def sum_of_ascii(input_string):
    return sum(map(ord, input_string))

q=sum_of_ascii('mananya')
print(q)

#to return the which take two strings as i put as username and psswd

def generate_psswd(username, psswd):
    num=username[0:4]+psswd[-4:]
    return num

a=generate_psswd('mananya','123456')
print(a)

##check the sequence of the string is correct according to the alphabetical sequence or not and print the times their are changes in the order
def count consequent (string)
string = string-lower()
count =0
for i in range(len(string) -1) :
    if ord (string[i]) == ord (string[i+1])-1:
        count +=1
    return count
    result = count consequent('abcfde")
    print(result)

##return the even numbers of the string
lst=[100,89,34,42]

def even(lst):
    for i in lst:
        if i%2==0:
            print(i)

print(even(lst))

















