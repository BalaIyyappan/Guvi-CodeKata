s=input().split()
l=len(s)
i=-1
for j in range(l):
  if j==l:
    print(s[i])
  else:
    print(s[i],end=" ")
  i=i-1
