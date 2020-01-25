n=int(input())
p=1
j=1
for i in range(1,n+1):
  if i==1:
    print(p)  
  else:
    j=j+2
    for k in range(j):
      if k!=j:
        print(p,end=" ")
      else:
        print(p)  
    print()
