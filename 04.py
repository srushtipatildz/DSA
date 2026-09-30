#Cube sum of n natural numbers
n=int(input("enter n: "))
arr=[]
sum=0
for i in range(n):
    x=int(input("Enter Number: "))
    arr.append(x)
    sum=sum+(x**3) #x**3 means x cube
print(sum)   