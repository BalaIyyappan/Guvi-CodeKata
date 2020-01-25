n=int(input())
mylist=[]
mylist.extend(input().split())
for i in mylist:
    count=mylist.count(i)
    if(count==1):
        print (i)
