#WAP to accept n integers into an array and calculate sum of all the elements:
n=int(input("Enter n"))
arr=[]
for i in range (n):
    x=int(input("Enter Number: "))
    arr.append(x)
    sum=0
    for j in arr:
     sum=sum+j;
print("Arr:",arr)
print(sum)
