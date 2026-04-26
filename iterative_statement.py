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
#     count=0
#     while n>0 :
#         count=count+1
#         n=n//10
#     print(count)
# else :
#     print("Negative no not allowed")

# 6.Sum of digits of a number
# n=int(input("Enter any no : "))
# sum=0
# if n>0 :
#     while n>0 :
#         digit=n%10
#         sum+=digit
#         n=n//10
#     print(sum)
# else :
#     print(f"Negative number {n} not allowed")

# 7.Check palindrome number
# n=int(input("Enter any no : "))
# x,rev=n,0
# while n>0 :
#     digit=n%10
#     rev=rev*10+digit
#     n=n//10
# if x==rev :
#     print("Palindrome")
# else :
#     print("Not Palindrome")

# 8.Keep asking input until negative number
# n=int(input("Enter any no : "))
# while n>=0 :
#     n=int(input("Enter number : "))

# print("User entered negative number , loop stopped ...")

# 9.Password checker
# correct_password = "python123"
# password = input("Enter password: ")
# while password != correct_password:
#     password = input("Wrong password, try again: ")

# print("Access granted")

# 10.Fibonacci series up to n terms
# n=10
# a,b=0,1
# count=0
# while count<n :
#     print(a,end=" ")
#     a,b=b,a+b
#     count+=1

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

# l=eval(input("Enter any list : "))     #new list ki wjh se space complexity increase ho rhi hn
# l1=[]
# for i in l :
#     l1.append(i+5)
# print(l1)

# l=eval(input("Enter any list : "))      #new list ki wjh se space complexity increase ho rhi hn
# l1=[]
# for i in l :
#     l1.append(i**2)
# print(l1)

# t=(1,2,3,4,5)
# l=list(t)
# print(l)
# print(type(l))
# l1=[]
# for i in l :
#     l1.append(i+5)
# t=tuple(l1)
# print(t)

# l=[1,2,3,4,5]
# l[0]=6
# print(l)

# l=[1,2,3,4,5]
# for i in range(len(l)) :
#     x=l[i]+5
#     l[i]=x
# print(l)

# l=[1,2,3,4,5]
# for i in range(len(l)) :
#     l[i]=l[i]+5
# print(l)

# d={"x":10,"y":20,"z":"python"}
# for i in d :
#     print(i)

# d={"x":10,"y":20,"z":"python"}
# for i in d :
#     print(i,'=',d[i])

# d={"x":10,"y":20,"z":"python"}
# for i in d.keys() :
#     print(i)

# d={"x":10,"y":20,"z":"python"}
# for i in d.values() :
#     print(i)

# d={"x":10,"y":20,"z":"python"}
# for i in d :
#     print(d[i])

# d={"x":10,"y":20,"z":"python"}
# for i,j in d.items() :
#     print(i,'=',j)

# s={10,20,30,'python','java'}
# for i in s :
#     print(i)

# QUESTIONS :
# 1.Print numbers from 1 to 10 using a for loop
# for i in range(1,11) :
#     print(i)

# 2.Print all even numbers from 1 to 20
# for i in range(1,21) :
#     if i%2==0 :
#         print(i,end=" ")

# 3.Print the multiplication table of 5
# for i in range(1,11) :
#     print(f'5 * {i} = {5*i}')

# 4.Print each character of a string (e.g., "Python")
# s="python"
# for i in s :
#     print(i)

# 5.Find the sum of numbers from 1 to 100
# sum=0
# for i in range(1,101) :
#     sum+=i
# print(sum)

# 6.Print all odd numbers between 1 and 50
# for i in range(1,51) :
#     if i%2!=0 :
#         print(i,end=" ")

# 7.Count how many vowels are in a string
# s="hello world WORLD"
# count=0
# for i in s :
#     if i.lower() in "aeiou" :
#         count+=1
# print(count)

# 8. Reverse a string
# s="python is a programming language"
# rev=" "
# for i in s :
#     rev=i+rev
# print(rev)

# 9. Factorial of a number.
# fact=1
# for i in range(1,6) :
#     fact*=i
# print(fact)

# 10. Pattern
# for i in range(1,6) :
#     print("*"*i+" "*(5-i))

# 11. Largest number in a list
# l=[1,8,7,6,5,80,9,0,8,59,43,2,3,7,9]
# largest=l[0]
# for i in l :
#     if i > largest :
#         largest=i
# print(largest)

# 12. Count digits in a number
# nums=3456789
# count=0
# for i in str(nums) :
#     count+=1
#     nums//=10
# print(count)

# 13. Fibonacci series
# n=10
# a,b=0,1
# for i in range(n) :
#     print(a,end=" ")
#     a,b=b,a+b

# 14. Prime number check
# n=19
# is_prime=True
# if n<=1 :
#     is_prime=False
# else :
#     for i in range(2,n) :
#         if n%i==0 :
#             is_prime=False
#             break
#     print(is_prime)

# 15. Remove duplicates from list
# nums = [1, 2, 2, 3, 4, 4, 5]
# unique = []
# for num in nums:
#     if num not in unique:
#         unique.append(num)
# print(unique)

# 16.Sum of digits of a number
# n=int(input("Enter a no : "))
# sum=0
# for i in range(1,n+1) :
#     digit=n%10
#     sum+=digit
#     n//=10
# print(sum)

# 17.Check if a number is palindrome
# n=int(input("Enter a no : "))
# x,rev=n,0
# while n>0 :
#     digit=n%10
#     rev=rev*10+digit
#     n//=10
# if rev==x :
#     print("Palindrome")
# else :
#     print("Not Palindrome")

# 18.Print all factors of a number
# n=int(input("Enter a no : "))
# for i in range(1,n+1) :
#     if n%i==0 :
#         print(i,end=" ")

# 19.Count words in a sentence
# s="Hello world python"
# s="Hello"
# count=1
# for i in s :
#     if i==" " :
#         count+=1
# print(count,end=" ")