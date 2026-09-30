#WAP to accept N integers into an array and display the largest,second largest,
#smallest and second smallest element!
n=int(input("Enter n :"))
arr=[]
for i in range (n):
    x=int(input("Enter Number :"))
    arr.append(x)
largest=arr[0]
smallest=arr[0]
for i in range(1,len(arr)):
     if(arr[i]>largest):
        slargest=largest
        largest=arr[i]
     if(arr[i]<smallest):
        s_smallest=smallest
        smallest=arr[i]   
print(arr)    
print("Largest:",largest)
print("Second Largest:",slargest)
print("Smallest:",smallest)
print("Second Smallest:",s_smallest)
