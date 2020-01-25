n=int(input())
l1=set(map(int,input().split()))
l2=set(map(int,input().split()))
result=l1.intersection(l2)

if len(result)==0:
  print(-1)
else:
  for i in result:
    print(i,end=" ")
