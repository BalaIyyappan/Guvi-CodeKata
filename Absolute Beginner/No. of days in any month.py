month={1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
m=int(input())
if m<=12 and m>=1:
  print(month[m])
else:
  print("Error")
