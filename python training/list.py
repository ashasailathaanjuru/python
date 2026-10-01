#list: list is a ordered mutable collection of elements.it is denoted by [](square brackets).it stores different types of elements.list can support inducting and slicing support
#eg:a=[1,2,3,4,5]
# s.append(60)
# s.insert(3,40)
# s.remove(5)
# print(s.count(5))
# print(s.index(40))
# print(s.pop())
# print(s)
#[]->string,float,bool,int,abc,tuple,list
# a=["a,b,c,100,500.0,true"]
# print(a)
# print(type(a))
# print(a[3])
# print(a[-5])
# print(a[100])#index error
# print(a[1:4])
# print(a[-1:-3:-2])
# print(a[::-1])

# b = list(range(1,11))
# print(b)

# c=([1,2,3,4,5,6,7,8,9,10])
# print(c)
# print(type(c))

#concadation
# a=[1,2,3]
# b=[4,5,6]
# print(a+b)

# #repetition 
# a=[1,2,3]
# b=3
# print(a*b)

# #membership
# a=[1,2,3]
# print(2 in a)
# print(37 in a)

# a=[1,2,3]
# b=[1,2,3]
# print(id(a))
# print(id(b))
# print(a is b)
x=[10,20,30,40,50]
x.append(60)
x.insert(2,500)
x.remove(10)
print(x.count(500))
print(x.index(20))
print(x.pop())
print(x)

n3=[10,20,30]
n3.append(50)
n3.append(100)
print(n3)

#insert
n4=[1,2,3,4]
n4.insert(1,100)
n4.insert(-100,111)
n4.insert(-10,111)
print('n4')
#extend
order1=['python','ReactJs','nextjs']
order1.extend('mySQL')
print(order1)
# remove
n5=[10,20,30,10,20,10,20]
n5.remove(10)
print(n5)
#pop();
l=[10,20,30,40]
print(l.pop())
print(l.pop())
print(l.pop())