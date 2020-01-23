n=int(input())
if(n>0):
  for i in range(1,n+1):
    if(i==n):
      print(9*i)
    else:
      print(9*i,end=" ")
else:
  print("NULL")
