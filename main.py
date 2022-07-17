name=input("enter your name")
college=input("enter your college name")
sem=input("enter your sem")
data='{name} {college} {sem}'.format(name=name, college=college, sem=sem)
print(data)

# name='mananya'
# collge='jecrc'

# print(name.upper())
# print(name.isdigit())
# #print(name.count(u))
# print(name.isnumeric())
# print(name.isprintable())
# print(name.isspace())
#
# sentence= f'{first_name} {name} is a coder

# lst= [1,3,5,7, 'HELLO',['a','b','c']]
# print(lst[0])
# print(lst)
# print(lst[-1])
# listt=[5,3,4,56,4,2,36,3,2]
# list.append('hello')
# listt.sort()
# print(listt)
# listt.sort(reverse=true)
# print(listt)

# listt.append('hello')
# print(listt)

#swapping the first and the last element of the list

# def swap_lst(new_lst):
#     size=len(new_lst)
#
#     # swapping
#     temp=new_lst[size-1]
#     new_lst[size-1]=new_lst[0]
#     temp=new_lst[0]
#
# new_lst=[3,132,43,56]
# print(swap_lst(new_lst))

# tuple
# list and tuple difference
# and strings are mutable or not
# sorting is not aplicable in set

# st= {1,2,5,67,4,4,7}
# st.union(bt)
# map_ ={
#     'first_name': 'mananya',
#     'last_name': 'gaur'
# }


# print(map_ (first_name))
# print(map_.get(last_name))
# print(map_.pop(first_name))
# print(map_.clear())
# print(map_.items())

#looping
lst=[1,2,3,4,5,6,7,9,87,4,7,10]
# for i in lst[2:]:
#     print(i)

# table=range(2,45)
# print(list(table))

# for i in 'Mananya':
#     print(i)

# for i in range(1,10):
#     print(i)

# for i in range(len(lst)):
#     print(lst[i])

#nested loops

# for i in range(len(lst)):
#     for j in ['a','b','c']:
#         print(i,j)

#prime number
# flag=False
# num = 23
# if num > 1:
#     for i in range(2, num):
#         if (num % i) == 0:
#             flag = True
#             break
#
# if flag:
#     print(num, "is not a prime number")
# else:
#     print(num, "is a prime number")
i=0
while i<5:
    print(i)
    i+=1
