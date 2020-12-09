#insert  random for the bombs
import random
#insert data from the user (mine , number)
table=[]
number=input("give Z (ZxZ) for the game-->")
mine=input("give number of mines-->")
if number%10!=0:
    number=number-number%10
################################
#i make the table of game
for i in range(number):
    table = ["    "]*number
cellgame=["mine"]* mine+["    "]*(number-mine)
random.shuffle(cellgame)
table = [cellgame[i:i+10] for i in range(0, number,10)]
#################################
#here i check whether the collum has any value. If it has value i will increase it, else i put the value "  1 "
def value(table,x,y):
    if table[x][y]=="  1 ":
        table[x][y]="  2 "
    elif table[x][y]=="  2 ":
        table[x][y]="  3 "
    else:
        table[x][y]="  1 "
#i check wheder it is inside the range and the variables x,y and table goes to fuction value
def restrictions(table,x,y):
    if 0<=x-1<len(table) and 0<=y<len(table[0]):
        value(table,x-1,y)
    if 0<=x<len(table) and 0<=y-1<len(table[0]):
        value(table,x,y-1)
    if 0<=x+1<len(table) and 0<=y<len(table[0]):
        value(table,x+1,y)
    if 0<=x<len(table) and 0<=y+1<len(table[0]):
        value(table,x,y+1)
    if 0<=x-1<len(table) and 0<=y-1<len(table[0]):
        value(table,x-1,y-1)
    if 0<=x+1<len(table) and 0<=y-1<len(table[0]):
        value(table,x+1,y-1)
    if 0<=x-1<len(table) and 0<=y+1<len(table[0]):
        value(table,x-1,y+1)
    if 0<=x+1<len(table) and 0<=y+1<len(table[0]):
        value(table,x+1,y+1)

#here I do the search amd when it finds it("nuke") goes to fuction restrictions
for x in range(len(table)):
    for y in range(len(table[x])):
        if table[x][y]=="mine":
            restrictions(table,x,y)
#here i print the table
for i in table:
        print i
