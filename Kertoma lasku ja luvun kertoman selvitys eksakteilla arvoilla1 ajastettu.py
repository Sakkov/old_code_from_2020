import time as t

n=1000*10

a=1

start_time1=t.process_time()

for _ in range(n):
    a=a*n
    n=n-1

print("\n",t.process_time()-start_time1)

start_time2=t.process_time()

d=0

while a>1:
    d+=1
    a=a//d
    
print("\n",d,"\n",t.process_time()-start_time2)