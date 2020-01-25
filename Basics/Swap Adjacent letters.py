name=input()
l=len(name)
ind=0
count=0
for i in name:
  while(count<l/2):
    j=ind+1
    print(name[j],end="")
    print(name[ind],end="")
    ind=ind+1
    count=count+1
