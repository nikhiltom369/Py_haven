limit=int(input("Enter Limit: "))
count=0
for i in range (2,limit+1):
    number=i
    flag=0
    for j in range(1,number+1):
        if number%j==0:
            flag+=1
    if(flag==2):
      count+=1
      print(number,end=" ")
print("\nCount of Prime Numbers: ",count)
