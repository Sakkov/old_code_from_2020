import time as t

n=26

a=1

start_time1=t.process_time()

for _ in range(n):
    a=a*n
    n=n-1

#print("\n",t.process_time()-start_time1)

start_time2=t.process_time()

len_zeros=str(a)
len_zeros=len(len_zeros) - len(len_zeros.rstrip('0'))

quess=len_zeros*5

print(a, len_zeros,quess)

c=25

while 1>0:
    if quess>=c:
        quess=quess-quess//c*5
        c=c*5
        print(quess)
        print(1)
    else:
        print(0)
        break

print("\n",quess,quess+1,quess+2,quess+3,quess+4,quess+5,"\n",t.process_time()-start_time2)