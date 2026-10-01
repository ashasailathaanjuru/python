#function: function is a group of statements repeatedly required we not recommed to write this statements every time separatly. we have to define this statements as a single unit and we call that unit any number of times based on our requirements with out rewritting
# function is a block of code design to perform a specific task.
#functions are 2 types.1.pre-defined functions(or)in built,2.user-defined functions
#1.in built:this functions are coming along with python software automatically are called as in built or pre-defined function
#eg:print(),input()
#2.user defined functions:the functions which are developed by programmers explictly according to there business required are called user-defined functions
#eg:def function_name() ,statements function, _name()
# def area(r):
#     result=22/7
#     area=result*r*r
#     print(area)
# area(7)
#Write a functions find the square of that number
# def square_number(x):
#     square_number=x*x
#     print(square_number)
# square_number(7)
#write a function calculate the shopping bill.{price*quality}
# def shopping_bill(price,quantity):
#     result=price*quantity
#     print("Your bill is:",result)
# shopping_bill(10,20)
# def number(x):
#     result=x%2==0
#     print(result)
# number(8)
# def number(y):
#     result=y%2!=0
#     print(result)
#     print(9)
#return statements: functions can take input as parameter and execute bussiness logic and return ouput with return statements
# def add(a,b):
#     return a+b
# result=add(5,3)
# print(result)
# #positional
# def greet(name,wish):
#     print("Hello",name,wish)
# greet('avinash','good morning')    

# def sum_sub(a,b):
#     sum=a+b
#     sub=a-b
#     result=sum,sub
#     print(result)
# sum_sub(100,500)
# sum_sub(500,100)

# def greet(name,wish):
#     print("hello",name,wish)

# greet(name='srikhar',
# wish='good afternoon')
# greet(wish='good afternoon',name='srikhar')    


# def greet(name,age,city):
#     print("hello",name,age,city)
# greet(name="asha",age="17",city="SKHT") 
# # default
# def greet(name='ravi',age='25'):
#     print('hello',name,age)
# greet()    

# def mul(a,b):
#     return a*b
# print(mul(3,4))
# def movie(hero,villian):
#     print('Hero:',hero)
#     print('villian:',villian)

# movie(hero='Mahesh',villian='prudhvi raj')

# def movie(hero='bob'):
#     print('hi',hero)
# movie()
# movie('pawan')
# variable-length(*)
# def f1(*a):
#     print(*a)
#     print(type(a))
# f1(10,20,30)
# def f2(n1,*s):
#     print(n1)
#     print(s)
# f2(10,'A',20,'B',30,'c')

# def f3(*s,n2):
#     print(s)
#     print(n2)
# f3(10,'A',20,'B',30,n2='c')    
#types of args:
# 1.Positional args:
# ------------------
#    *These are the Arguments passed to function in correct positional order.
#    *The no.of args and position of args must be matched .
#       If we change the order then the result will changed .
#       If we change the no.of args then we will get an error.

# 2.Keyword args:
# ---------------
#    *We can pass argument values by keyword i.e parameter name 
#    *Here the order of args is not important but number of args must be matched 

# Note:
# -----
# *We can use both positional and keyword argument simultaneosly.
# But first we have to take positional arguments then keyword args,
# otherwise we will get error

# 3.Default args:
# --------------
# *Sometimes we can provide default values for our positional args.
# *If we are not passing any name then only default value will be considered.

# 4.Variable-length args:
# ----------------------
# *Sometimes we can pass any no.of args to our function,
# such type of args are called as variable-length of args.
# *We can declare a variable length args with *symbol as:
#       def f1(*n):
# *We can call this function by passing any no.of args including zero,
#  internally all these values represented in the tuple.
# *After variable length arg,if we are taking any other args then we should provide values as keyword args.
# def f(arg1,arg2,arg3=4,arg4=8):
#     print(arg1,arg2,arg3,arg4)
# f(3,2)
# f(10,20,30,40)
# f(25,50,arg4=100)
# f(arg4=2,arg1=3,arg2=4)
# f()#error
# f(4,5,arg2=6)#error
# f(arg3=10,arg4=20)#error
# f(4,5,arg3=5,arg5=6)#type error

#** kwargs
# def f1(**a):
#     print(a)
#     print(type(a))
# f1(a=10,b=20,c=30,d=40)    
'''
Function: A group of lines with some name is called function.
a group of functions saved in one file is called module.
A group of module is nothing but a package.
A group of package is nothing but a library.
 In python there are 2 types of variable
types of variables
1.global variable
2.local variable

1.global variable: if the value of variable is defined outside a function such time of variable is called global variable
this variable can be access inside and outside of the function

variable_name=value
a='this is global variable'
b=10
def g()
print(a)
print(b)
 defg1()
 print(a)
 print(b)

 # local variable:  the Variables which are declared inside the function are called local variables.
 Local variables are available only for the in which function declared outside of variable we can't access
 def l()
 a="this is local"
 b=10
 print(a)
print(b)

def l1():
print(a)
print(b)
'''
# a='This is global variable'
# b=10
#creating a function
# def g():
#     print(a)
#     print(b)
#     # creating another function
# def g1():
#     print(a)
#     print(b)
# # calling function
# g()
# g1()       
# local variable
# def l():
#     a='This is local variable'
#     b=10
#     print(a)
#     print(b)
# # creating another function
# def l1():
#     print(a)
#     print(b)
# #calling a function
# l()
# l1()        
'''''
Lambda function
Anonymous function
----------------------------
*sometimes we can declare a function without name, such type of nameless
functions are called as anonymous functions or lambda expressions.
*The main advantage of anonymous function is just for instant use 
(i.e for one time usage)
syn:
lambda argument_list:expression
note:
by using lambda functions we can write concise code so that readability of the program will be improved.
note:
lambda function internally returns expression value and we are not required to write return statement explicitly.
 some times we can pass function as argument to another function.
 in such case lambda function are best choice

 we can use lambda functions very commonly with filter(),map() and reduce()
 functions bcoz these functions expect function as argument.


 # normal func:
 #----------------
 def squareit(n):
 return n*n
 print(squareit(3))
 print(squareit(4))
 ## lambda func:
 ##---------
 s=lambda n:n*n
 print('the square of 3 is:'s(3))
 print('the square of 5 is:,s(5))
'''
# s=lambda n:n+n
# print(s(5))
# x=lambda n: "even" if n%2==0 else "odd"
# print(x(8))

# p=lambda a,b:a if a>b else b
# a=8
# b=9
# result=p(a,b)
# print(result)
#calling a function itself is called recursive function
# normal function
# def factorial(n):
#     result=1
#     while n>=1:
#         result=result*n
#         n=n-1
#     return result
# print(factorial(5))
# recursive function
def fact(n):
    if n==0:
        return 1
    else:
        result=n*fact(n-1)
    return result
print(fact(5))
        

def is_palindrome(s):

    if len(s) <= 1:
        return True
    
    if s[0] != s[-1]:
        return False
    return is_palindrome(s[1:-1])
print(is_palindrome("racecar"))  
print(is_palindrome("python"))   
print(is_palindrome("noon"))
'''

'''





    





