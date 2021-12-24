import numpy as np
import time
start_time = time.time()

#Upper limit
n=np.uint64(10**4)
#Lower limit
m=n-1000

a = np.arange(n, dtype=np.uint64)

a=a[np.remainder(a,2)!=0]
a=a[np.remainder(a,3) != 0]
a=a[np.remainder(a,5) != 0]
a=a[np.remainder(a,7) != 0]
a=a[np.remainder(a,11) != 0]
a=a[np.remainder(a,13) != 0]
a=a[np.remainder(a,17) != 0]
a=a[np.remainder(a,23) != 0]
a=a[np.remainder(a,29) != 0]
a=a[np.remainder(a,31) != 0]
a=a[np.remainder(a,37) != 0]
a=a[np.remainder(a,41) != 0]


a=a[a > m]

count=0

#b=int(len(a)-len(a)*.1)
b=0

arr2=np.arange(n, dtype=np.uint64)
arr2=arr2[arr2 > 42]
arr2=arr2[np.remainder(arr2,2)!=0]
arr2=arr2[np.remainder(arr2,3) != 0]
arr2=arr2[np.remainder(arr2,5) != 0]
arr2=arr2[np.remainder(arr2,7) != 0]
arr2=arr2[np.remainder(arr2,11) != 0]
arr2=arr2[np.remainder(arr2,13) != 0]
arr2=arr2[np.remainder(arr2,17) != 0]
arr2=arr2[np.remainder(arr2,23) != 0]
arr2=arr2[np.remainder(arr2,29) != 0]
arr2=arr2[np.remainder(arr2,31) != 0]
arr2=arr2[np.remainder(arr2,37) != 0]
arr2=arr2[np.remainder(arr2,41) != 0]
#arr1=np.array([3,5,7,11,13,17,19])

for _ in range(int(m)):
    t=np.take(a,b)
    arr3=arr2[arr2<t]
    if np.all(np.remainder(t,arr3)!=0):
        biggestPrime=t
        print (t)
        count+=1
    b+=1
    if b==len(a):
        break
    
print("\n"+str(b))
print(count)
#print(int(n-n*.1))
#print(a)
try:
    biggestPrime
except NameError:
    print("No Primes Found between numbers "+str(m)+" - "+str(n))    
else:
    print("Lenght of The Greatest Prime "+str(len(str(biggestPrime))))#printataan suurimman primen pituus
    
    print("\nThe Greatest Prime Calculated is "+str(biggestPrime))#printtaa suurin löydetty prime

print ("\nMy program took", time.time() - start_time, "seconds to run")