# Dictonary: it is a ordered and mutable tcollection of elements. it is denoted by
'''
*it is a ordered and mutable collection of elements.
*it is denoted by{}.
*it represents the key value pair in the dictionary.
*insertion order is preserved.
*hetrogenious objects are allowed.
*duplicate are not allowed.
*indexing and slicing are not allowed.

*when list and tuple comparison by default datatype is"tuple".
*when set and dictionary comparison by default datatype is "dictionary".
*we can use list,tuple,and set to represent a group of individual objects as a single entity.
*if we want to represent a group of objects key-value pairs then we should go for dict.
'''
'''
FUNCTIONS
1.len()
2.count()
3.get()
4.pop()
5.remove()
6.keys()
7.values()
'''
#creating dict
d1=dict({100:'avinash',200:'srikhar',300:'kiran'})
print(d1)
d2=dict({(333,'mohit'),(666,'sai charan'),(999,'abhi')})
print(d2)
d3=dict((('l','ravi'),('r','uday'),('s','sunny')))
print(d3)
#len()
d1=dict({100:'mohit',200:'sai charan',300:'abhi'})
print(len(d1))
#clear
d1=dict({100:'mohit',200:'sai charan',300:'abhi'})
print(d1.clear())
#get
d1=dict({100:'mohit',200:'bunny',300:'abhi'})
d={100:'mohit',200:'bunny',300:'abhi'}
print(d[100])
# print(d[400])#key error
print(d.get(100))
print(d.get(400))#none
print(d.get(100,'mohit'))
print(d.get(400,'mohit'))
#pop
d={100:'mohit',200:'bunny',300:'abhi'}
print(d.pop(300))
# print(d.pop(400))#key error
#popitem
d={100:'mohit',200:'bunny',300:'abhi'}
print(d.popitem())

d={}
# print(d.popitem())#keyerror
#key
d={100:'mohit',200:'bunny',300:'abhi'}
print(d.keys())
for k in d.keys():
    print(k)
#values
d={100:'mohit',200:'bunny',300:'abhi'}
print(d.values())
for k in d.values():
    print(k)

    d={100:'mohit',200:'bunny',300:'abhi'}
    print(d.items())
    for k,v in d.items():
        print(k,'--->',v)
#copy
d={100:'mohit',200:'bunny',300:'abhi'}
d1=d.copy()
print(id(d))
print(id(d1))
#setdefault
d={100:'mohit',200:'bunny',300:'abhi'}
print(d.setdefault(100,'mohit'))
print(d.setdefault(400,'vamsi'))
#print(d)

#update
d={100:'mohit',200:'bunny',300:'abhi'}
d1={'a':'apple'}
d.update(d1)
print(d)
d.update([(333,'A')])
print(d)