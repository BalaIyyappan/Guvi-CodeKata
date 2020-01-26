alpha=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
plate=input()
s=0
for i in plate:
  if(i.lower() in alpha):
    pass
  else:
    if(i=='-'):
      pass
    else:
      i=int(i)
      s=s+i
print(s)
