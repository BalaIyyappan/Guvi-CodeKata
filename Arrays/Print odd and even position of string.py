s=input()
l=len(s)
j=1
s1=[]
s2=[]
for i in s:
  if j%2!=0:
    s1.append(i)
    j=j+1
  else:
    s2.append(i)
    j=j+1

for j in s1:
  print(j,end="")
print(end=" ")
for k in s2:
  print(k,end="")
