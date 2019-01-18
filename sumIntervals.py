def sumIntervals(n):
    sum=0
    #i sort the list and find the minimum
    n.sort()
    print n
    last_number=n[0]
    last_number=last_number[0]
    sum=0
    y=len(n)
    for i in range(1,y):
        x=n[i]
        z=n[i-1]
        if x[0]<z[1]:
            #if the next first item is less than the last one in the previous list and if the next item is even smaller than the previous list
            if x[1]<z[1]:
                #i calculate the last distance
                sum=sum +(z[1]-last_number)
                last_number=z[1]
            else:
                #else i calculate the distance from the last number to last_number
                sum=sum +(x[1]-last_number)
                last_number=x[1]
        elif x[0]>z[1]:
            #if the next first item is bigger than the last one in the previous list i calculate the next distance
                if i==1:
                    #if hapen this in first time i calculate the first distance
                    sum=sum+(z[1]-z[0])
                sum=sum+(x[1]-x[0])
                last_number=x[1]
    print "sum",sum
n=input("give me distance inside the function sumIntervals-->")
