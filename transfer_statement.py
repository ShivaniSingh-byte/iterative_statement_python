# Transfer statement : cursor ko ek jgh se dusri jgh pe bhjne ke liye transfer statement ka use krte hn
# continue : skip current iteration
# break : terminate current loop
# pass : skip current block

# for i in range(5) :
#     if i==0 :
#         continue
#     print("Hello")

# for i in range(5) :
#     if i==0 :
#         break
#     print("Hello")

# for i in range(5) :
#     if i==0 :
#         pass
#     print("Hello")

# n=10
# i=1
# while i<=n : 
#     if i==5 :
#         continue
#     print(i)
#     i=i+1

# n=10
# i=1
# while i<=n : 
#     i=i+1
#     if i==5 :
#         continue
#     print(i)

# n=10
# for i in range(1,11) :
#     if i==5 :
#         continue
#     print(i)

# n=int(input("Enter a no : "))
# i=1
# while i<=n :
#     if i==5 :
#         pass
#     else :
#         print(i,end=" ")
#     i=i+1

# n=int(input("Enter a no : "))
# i=1
# while i<=n :
#     if i==5 :
#         break
#     else :
#         print(i,end=" ")
#     i=i+1
# print("Hello")

# for i in range(1,11) :
#     if i==3 :
#         break
#     else :
#         print(i)
# print("Hello")

# CALCULATOR :
while True :
    print(" 1. Addition\n 2. Substarction\n 3. Multiplication\n 4. Division\n 5. OFF")
    n=int(input("Enter above mention any one option : "))
    # if n==1 or n==2 or n==3 or n==4 or n==5 :
    num=[1,2,3,4,5]
    if n in num :
        if n==1 :
            x=int(input("Enter how many numbers you want to add : "))
            sum=0
            for i in range(1,x+1) :
                number=int(input(f"Enter {i} number : "))
                sum=sum+number
            print("Addition is : ",sum)

        elif n==2 :
            x=int(input("Enter how many numbers you want to add : "))
            sub=0
            for i in range(1,x+1) :
                number=int(input(f"Enter {i} number : "))
                sub=number-sub
            print("Substraction is : ",sub)
        
        elif n==3 :
            x=int(input("Enter how many numbers you want to add : "))
            mul=1
            for i in range(1,x+1) :
                number=int(input(f"Enter {i} number : "))
                mul=mul*number
            print("Multiplication is : ",mul)

        elif n==4 :
            x=int(input("Enter how many numbers you want to add : "))
            div=1
            for i in range(1,x+1) :
                number=int(input(f"Enter {i} number : "))
                div=number/div
            print("Division is : ",div)
        
        else :
            break

    else :
        print("Please enter valid option")

# n=5
# l=[]
# for i in range(1,n+1) :
#     num=int(input("Enter a no : "))
#     l.append(number)
#     sum=sum+num
# print(f'Addition of given no {l} is {sum}')
        