# ITERATIVE STATEMENT :
# to avoid the repeation of block of code and then we use the iterative statement
# 1.for loop : finite iteration,collection datatype
# 2.while loop : infinite iteration 

# WHILE LOOP :
# syntax : while condition :
#             | while body 
# example : while True :
#     print("Hello")

# start_point
# while terminating_point :
#     |
#     | while_body
#     |
#     increment/decrement
#     i=i+1 i=i-1

# NUMBERS :
# n=eval(input("Enter any no : "))
# i=1
# while i<=n :
#     print(i,end=" ")
#     i=i+1

# n=eval(input("Enter any no : "))
# i=1
# sum=0
# while i<=n :
#     if i<n :
#         print(i,end=",")
#     else :
#         print(i)
#     i=i+1

# n=eval(input("Enter any no : "))
# i=1
# sum=0
# while i<=n :
#     if i<n :
#         print(i,end="+")
#     else :
#         print(i)
#     i=i+1

# n=eval(input("Enter any no : "))
# i=1
# sum=0
# while i<=n :
#     if i<n :
#         print(i,end="+")
#     else :
#         print(i,end="=")
#     i=i+1

# n=eval(input("Enter any no : "))
# i=1
# sum=0
# while i<=n :
#     sum=sum+i
#     if i<n :
#         print(i,end="+")
#     else :
#         print(i,end="=")
#     i=i+1
# print(sum)

# n=eval(input("Enter any no : "))
# i=1
# sum=1
# while i<=n :
#     sum=sum*i
#     if i<n :
#         print(i,end="*")
#     else :
#         print(i,end="=")
#     i=i+1
# print(sum)

# EVEN :
# n=eval(input("Enter any no : "))
# i=2
# while i<=n :
    # if i<n :
    #     print(i,end=",")
    # else :
    #     print(i)
#     i=i+2

# n=eval(input("Enter any no : "))
# i,sum=2,0
# while i<=n :
#     sum=sum+i
    # if i<n :
    #     print(i,end="+")
    # else :
    #     print(i,end="=")
#     i=i+2
# print(sum)

# n=eval(input("Enter any no : "))
# i,mul=2,1
# while i<=n :
    # mul*=i
    # if i<n :
    #     print(i,end="*")
    # else :
    #     print(i,end="=")
#     i=i+2
# print(mul)

# ODD :
# n=eval(input("Enter any no : "))
# i=1
# while i<=n :
#     if i<n-1 :
#         print(i,end=",")
#     else :
#         print(i)
#     i=i+2

# n=eval(input("Enter any no : "))
# i,sum=1,0
# while i<=n :
#     sum+=i
#     if i<n-1 :
#         print(i,end="+")
#     else :
#         print(i,end="=")
#     i=i+2
# print(sum)

# n=eval(input("Enter any no : "))
# i,mul=1,1
# while i<=n :
#     mul*=i
#     if i<n-1 :
#         print(i,end="*")
#     else :
#         print(i,end="=")
#     i=i+2
# print(mul)

# n=int(input("Enter any no : "))
# s=str(n)
# print(type(s))
# print("Total digits are : ",len(s))

# //floor division se last digit haat jati hn
# %modulous remainder dikhta hn
# count a digits
# n=int(input("Enter any no : "))
# count=0
# while n>0 :
#     count+=1
#     n=n//10
# print(f'Total digits are {count}')

# sum of a digit :
# n=int(input("Enter any no : "))
# if n>0 :
#     sum=0
#     while n>0 :
#         digit=n%10
#         sum+=digit
#         n=n//10
#     print(f'Total sum of digits : ',sum)
# else :
#     print("please provide valid no")

# ARMSTRONG :
# n=int(input("Enter a no : "))
# x,y,td,sum=n,n,0,0
# while n>0 :
#     td=td+1
#     n=n//10
# while x>0 :
#     ld=x%10
#     sum=sum+ld**td
#     x=x//10
# if y==sum :
#     print("Armstrong Number")
# else :
#     print("Not an armstrong number")

# PALINDROME : # string case
# n=input("Enter any no : ")
# if n==n[::-1] :
#     print("Palindrome")
# else :
#     print("Not Palindrome")

# Number case :
# n=int(input("Enter any no : "))
# rev,x=0,n
# while n>0 :
#     ld=n%10
#     rev=rev*10+ld
#     n=n//10
# if x==rev :
#     print("Palindrome")
# else :
#     print("Not Palindrome")

# QUESTIONS :
# 1.Print numbers from 1 to 10 using a while loop.
# n=int(input("Enter any no : "))
# i=1
# if n>0 :
#     while i<=n :
#         print(i,end=" ")
#         i=i+1
# else :
#     print("Negative no not allowed")

# 2.Print all even numbers from 1 to 50.
# n=int(input("Enter any no : "))
# i=2
# if n>0 :
#     while i<=n :
#         print(i,end=" ")
#         i+=2
# else :
#     print("Negative no not allowed")

# 3.Print the multiplication table of a given number (e.g., 5).
# n=int(input("Enter any no : "))
# i=1
# if n>0 :
#     while i<=10 :
#         print(f'{n} * {i} : {n*i}')
#         i+=1
# else :
#     print("Please provide a valid no ")

# 4.Reverse a number using a while loop (e.g., 123 → 321).
# n=int(input("Enter any no : "))
# rev=0
# if n>0 :
#     while n>0 :
#         digit=n%10
#         rev=rev*10+digit
#         n=n//10
#     print(rev)
# else :
#     print("Negative no not allowed")

# 5.Count the number of digits in a number.
# n=int(input("Enter any no : "))
# if n>0 :
#     sum=0
#     while n>0 :
#         digit=n%10
#         sum+=digit
#         n=n//10
#     print(sum)
# else :
#     print("Negative no not allowed")

# FOR LOOP : 
# syntax : for variable in iterables:-collection datatype(list,tuple,string,dict,range)
#                 | for_body

# s=input("Enter any word : ")
# for ch in s :
    # print(ch)
    # print(chr(ord(ch)+1))

# s=input("Enter any word : ")
# s1=""
# for ch in s :
#     s1=s1+chr(ord(ch)+1)
# print(s1)

# s=input("Enter any word : ")
# for ch in s :
#     s=s.join(s)+chr(ord(ch)+1)
# print(s)