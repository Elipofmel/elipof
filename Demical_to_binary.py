a=int(input('enter a num:'))
p=1
result=0
while a>0:
   x=a%2
   result=result+(x*p)
   a=a//2
   p=p*10
print(result)
    
