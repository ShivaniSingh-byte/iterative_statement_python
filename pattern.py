# PATTRENS :

# n=int(input("Enter any no : "))
# i=1
# while i<=n :
#     print("*"*n)
#     i=i+1

# ONE :
# n=int(input("Enter any no : "))
# i=1
# while i<=n :
#     print("*"*i+" "*(n-i))
#     # print("*"*i)
#     i=i+1

# TWO :
# n=int(input("Enter any no : "))
# i=1
# while i<=n :
#     print(" "*(n-i)+"*"*i)
#     i=i+1

# THREE :
# n=int(input("Enter any no : "))
# i=1
# while i<=n :
#     print(" "*(n-i)+"* "*i)
#     i=i+1

# FOUR :
# n=int(input("Enter any no : "))
# i=0
# while i<n :
    # print('*'*(n-i)+' '*i)
    # print('*'*(n-i))
    # i=i+1

# FIVE :
# n=int(input("Enter any no : "))
# i=0
# while i<n :
#     print(' '*i+'*'*(n-i))
#     i=i+1

# SIX :
# n=int(input("Enter any no : "))
# i=0
# while i<n :
#     print(' '*i+'* '*(n-i))
#     i=i+1

# ONE & FOUR :
# n=int(input("Enter any no : "))
# i=1
# while i<=n :
#     print('* '*i+' '*(n-i))
#     i=i+1
# # print(i) #6 
# i=i-2
# while i>0 :
#     print('* '*i+' '*(n-i))
#     i=i-1

# TWO & FIVE :
# n=int(input("Enter any no : "))
# i=1
# while i<=n :
#     print(' '*(n-i)+'*'*i)
#     i=i+1
# # print(i) #6 
# i=i-2
# while i>0 :
#     print(' '*(n-i)+'*'*i)
#     i=i-1

# THREE & SIX :
# n=int(input("Enter any no : "))
# i=1
# while i<=n :
#     print(' '*(n-i)+' *'*i)
#     i=i+1
# # print(i) #6 
# i=i-2
# while i>0 :
#     print(' '*(n-i)+' *'*i)
#     i=i-1

# n=int(input("Enter any no : "))
# for i in range(1,n+1) :
#     print('*'*i+' '*(n-i))

# n=int(input("Enter any no : "))
# for i in range(1,n+1) :
#     print(' '*(n-i)+'*'*i)

# n=int(input("Enter any no : "))
# for i in range(1,n+1) :
#     print(' '*(n-i)+'* '*i)

# n=int(input("Enter a no : "))
# # for i in range(5) : #0,1,2,3,4
# for i in range(1,n+1) :
#     for j in range(1,n+1) :
#         print(j,end=" ")
#     print()

# n=int(input("Enter a no : "))
# for i in range(1,n+1) :
#     for j in range(1,i+1) :
#         print(j,end=" ")
#     print()

# n=int(input("Enter a no : "))
# x=1
# for i in range(1,n+1) :
#     for _ in range(1,i+1) :
#         print(x,end=" ")
#         x+=1
#     print()

# n=int(input("Enter a no : "))
# x=2
# for i in range(1,n+1) :
#     for _ in range(1,i+1) :
#         print(x,end=" ")
#         x+=2
#     print()

# n=int(input("Enter a no : "))
# x=1
# for i in range(1,n+1) :
#     for _ in range(1,i+1) :
#         print(x,end=" ")
#         x+=2
#     print()

# n=int(input("Enter a no : "))
# for i in range(1,n+1) :
#     ch='A'
#     for _ in range(1,i+1) :
#         print(ch,end=" ")
#         ch=chr(ord(ch)+1)
#     print()

# n=int(input("Enter a no : "))
# ch=input("Enter any character : ")
# for i in range(1,n+1) :
#     for _ in range(1,i+1) :
#         print(ch,end=" ")
#         ch=chr(ord(ch)+1)
#     print()

# n=int(input("Enter a no : "))
# ch=input("Enter any character : ")
# for i in range(1,n+1) :
#     for _ in range(1,i+1) :
#         print(ch,end=" ")
#         ch=chr(ord(ch)+1)
#     print()

# n=int(input("Enter a no : "))
# ch=input("Enter a single character : ")
# for i in range(n,0,-1) :
#     ch1=ch
#     for j in range(1,i+1) :
#         print(ch1,end=" ")
#         ch1=chr(ord(ch1)+1)
#     print()

# n=int(input("Enter a no : "))
# ch=input("Enter a single character : ")
# for i in range(n,0,-1) :
#     print(" " * (n - i), end="")
#     ch1=ch
#     for j in range(1,i+1) :
#         print(ch1,end=" ")
#         ch1=chr(ord(ch1)+1)
#     print()

# n = int(input("Enter a no : "))
# ch = input("Enter any character : ")
# for i in range(1, n+1):
#     print(" " * (n - i), end="")   # spaces
#     temp = ch
#     for j in range(i):
#         print(temp, end=" ")
#         temp = chr(ord(temp) + 1)
#     print()

# n = 4
# ch = 'a'
# for i in range(n):
#     temp = chr(ord(ch) + i)
#     for j in range(i+1):
#         print(temp, end=" ")
#         temp = chr(ord(temp) - 1)
#     print()

# n=int(input("Enter a no : "))
# for i in range(1,n+1) :
#     print("*"*i+" "*(n-i))

# n=int(input("Enter a no : "))
# for i in range(1,n+1) :
#     print(" "*(n-i)+"*"*i)

# n=int(input("Enter a no : "))
# for i in range(n) : 
#     print("*"*(n-i)+" "*i)

# n=int(input("Enter a no : "))
# for i in range(n) : 
#     print(" "*i+"*"*(n-i))
