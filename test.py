#anaconda
#qianwen
#cainiao

s1=input().split()
num1=tuple(s1)
l1=len(num1)

s2=input().split()
num2=tuple(s2)
l2=len(num2)


a=l1/2
b=l2/2
int(a)
int(b)
if(l1%2!=0):
    print(num1[l1//2])
else:
    print((num1[a]+num1[a+1])/2)


if(l2%2!=0):
    print(num1[l2//2])
else:
    print((num1[b]+num1[b+1])/2)


