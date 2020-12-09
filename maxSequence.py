def maxSequence(n):
    x=len(n)
    max=-10**4
    z=[]
    #1.find the length of list for the range
    #2.I put in var max a very small value
    for i in range(x):
        #3.initalization the var sum and the list z
        sum=0
        z[:]=[]
        for j in range(i,x):
            #4.in this loop the var sum is increase by n[j] and is append in list z
            sum=sum+n[j]
            z.append(n[j])
            if sum>max:
                #5.when sum is max in var mxl(maxlist) assigned the list z
                max=sum
                mxl=z[:]
    print "max number-->",max
    print "max list:->",mxl
n=input("give function maxSequence-->")
