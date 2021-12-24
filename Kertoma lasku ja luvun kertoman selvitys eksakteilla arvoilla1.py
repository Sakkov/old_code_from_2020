n=10000

a=1

for _ in range(n):
    a=a*n
    n=n-1

print("\n",a)

d=0

while a>1:
    d+=1
    a=a//d
    
print(d)