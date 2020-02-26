
for num in range(50,200):
    i=num
    count=0
    while(i>=1):
        if(num%i==0):
            count=count+1
        i=i-1
    if(count==2):
        print(num)
