num=input()
c1=0
c2=0
c3=0
c4=0
c5=0
c6=0
c7=0
c8=0
c9=0
c0=0
if '1' in num:
    c1=1
if '2' in num:
    c2=1
if '3' in num:
    c3=1
if '4' in num:
    c4=1
if '5' in num:
    c5=1
if '6' in num:
    c6=1
if '7' in num:
    c7=1
if '8' in num:
    c8=1
if '9' in num:
    c9=1
if '0' in num:
    c0=1

s=0
s=c1+c2+c3+c4+c5+c6+c7+c8+c9+c0
if s==2:
    print('Saturated')
else:
    print('Unsaturated')
