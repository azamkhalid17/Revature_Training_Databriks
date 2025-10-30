
sqarelist=[]
list1=[10,20,20,40]
for i in list1:
    sqarelist.append(i*i)
print(sqarelist)
tuple1=tuple(sqarelist)
print(tuple1)

dict1=dict()
list2=[1,2,3,4,5,6]
for i in list2:
    dict1[i]=i*i
print("****dict1 print******")
print(dict1)
print("****dict1 print collom form******")
for k,v in dict1.items():
    print(k,v)
print("****dict1 key print****")
for k in dict1.keys():
    print(k)
print("****dict1 value print******")
for v in dict1.values():
    print(v)



