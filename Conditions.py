
fname='mananya'
lname="gaur"

#Use of AND condition
if fname=="mananya" and not lname=="gaur":
    print('yes first name is mananya gaur')
else:
    print('first name is not mananya')
#
# #use of OR condintion
if fname=="mananya" or not lname=="gaur":
    print('yes first name is mananya gaur')
else:
    print('first name is not mananya')

#Use of elif condition
if 'mananya' in ['a','b','c']:
    print("print mananya is on the list")
elif 'p' in 'mananya':
    print("print mananya is on the list")
else:
    print('kuch bhi ni mila')


#take a input from user and print the character only whose ASCII value is even
s=input ("enter the string")
for i in s:
    if ord(i) % 2 == 0:
        print("the ASCII value is even of " + i)
    else:
        print("The ASCII value is not even ")

#take 5 inputs from the user and append them into the list
n=input("Enter a number")
a=int(n)
lst=[]
for i in range (0,a):
    num=input("enter input")
    lst.append(num)
print(lst)

#take n(int) input from the user and then again in the loop take n*2 inputs from the user, thne arrange hese inputs as the dictionary in which
#keys will be the data types which are the odd inputs and values will be the inputs which are the even inputs.

n=input("enter a numer")
a=int(n)
dict={
    'str': [],
    'int': [],
    'float': []
}
lst=[]
for i in range (0,a):
    num=input("Enter the data type for the value")
    val=input("Enter the value with respect to the data type")
    if num =='str':
        dict['str'].append(val)
    elif num =='int':
        dict['int'].append(val)
    elif num == 'float':
        dict['float'].append(val)
    else:
        print('please initialse an empty list for {num}'.format(num=num))

print(dict)










