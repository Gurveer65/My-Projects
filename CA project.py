import random 
a=int(input("Enter left limit: "))
b=int(input("Enter right limit: "))
n=random.randint(a,b)
print("Range is (",a,",",b,") and randomly picked number is ",n)
if (n%2==0):
    print(n,"is an even number\n")
else:
    print(n,"is an odd number\n")
if (n>=0):
    print(n,"is a positive number\n")
else:
    print(n,"is a negative number\n")
c=0
for i in range(2,n):
    if(n%i==0):
        print(n,"is a composite number\n")
    c=1
    break
    if(c==0):
        print(n,"is a prime number\n")
    
from math import sqrt
sq_root=int(sqrt(n))
if (sq_root*sq_root)==n:
    print(n,"is a perfect square\n")
else:
    print(n,"is not a perfect square\n")

order=len(str(n))
sum=0
temp=n
while temp>0:
    digit=temp%10
    sum+=digit**order
    temp//=10
if n==sum:
    print(n,"is an Armstrong number\n")
else:
    print(n,"is not an Armstrong number\n")
    
temp=n
rev=0
while(n>0):
    dig=n%10
    rev=rev*10+dig
    n=n//10
if(temp==rev):
    print(temp,"is a palindrome\n")
else:
    print(temp,"isn't a palindrome\n")
    







        