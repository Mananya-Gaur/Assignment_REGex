#In the given string then find out the frequency of the character in the string by making a dictionary .

s=input("Enter a string")
s=s.lower()
dict={}
for i in s:
    a=s.count(i)
    dict[i]=a
print(dict)

##or
s=input("Enter a string")
s=s.lower()
dict={}
for i in s:
    if i in dict:
        dict[i] += 1
    else:
        dict[i]=1
print(dict)

##take inputs from the user of push and pop and accordinly append and pop the values in the list and break the loop only if we got input as stop
lst=[]
while True:
    s=input("enter the command and numbers")
    s=s.split()
    print(s)
    if s[0]=='push':
        lst.append(s[1:])
    elif s[0]=='pop':
        lst.remove(s[1:])
    elif s[0]=='stop':
        break
print(lst)

##take inputs from the user in string as subject and students the put them into dictionary in which the values will be in the form of sets
map_ = {}
while True:
    stud_info = input("enter the subject and students")

    stud_info = stud_info.split()
    if stud_info[0] == 'stop':
        break
    else:
        if stud_info[0] in map_:
            map_[stud_info[0]].add(stud_info[1])
        else:
            map_[stud_info[0]] = {stud_info[1]}
            # map_[stud_info[0]].add(stud_info[1])

print(map_)
