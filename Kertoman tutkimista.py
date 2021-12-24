n=100
n=n+1

a=1
b=1

for _ in range(n):
    len_zeros=str(a)
    len_zeros=len(len_zeros) - len(len_zeros.rstrip('0'))
    quess=len_zeros*5
     
    c=25

    while 1>0:
        if quess>=c:
            quess=quess-quess//c*5
            c=c*5
        else:
            break
    print("\n\n",b-1,len_zeros,len_zeros*5,quess)
    
    if quess<=b-1 and quess+5>=b-1:
        print("yes")
    
    a=a*b
    b=b+1
