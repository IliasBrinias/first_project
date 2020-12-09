n=raw_input("give something to calculate-->")
#i split the text
z=[]
z=n.split("(")
z.pop()
written_in_full=["zero","one.","two","three","four","five","six","seven","eight","nine"]
number=[0,1,2,3,4,5,6,7,8,9]
operators=["plus","minus","times"]
#i find these tow numbers
for i in range(len(number)):
    if z[0]==written_in_full[i]:
        num1=number[i]
    if z[2]==written_in_full[i]:
        num2=number[i]
#i find the operator and then the variable total
for i in range(len(operators)):
    if z[1]==operators[0]:
        total=num1+num2
    elif z[1]==operators[1]:
        total=num1-num2
    elif z[1]==operators[2]:
        total=num1*num2
print   "total:", total
