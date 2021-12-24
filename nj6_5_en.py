import numpy as np
import math as ma
import re

regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')

urd = lambda i: ord(i)

vurd = np.vectorize(urd)

stri = lambda i: str(i)

vstri =np.vectorize(stri)

while True:
    try:
        m=int(input("The base of the number system of your number in base 10:"))
        if 0<m<=62:
            break
        elif m<=0 or m>62:
            print("The base must be in range [1,62]")
    except ValueError:
        print("Give the base number in base 10")

if 0<m<10:
    mm=m
elif 10<=m<36:
    mm=chr(64+m-9)
elif 36<=m<63:
    mm=chr(96+m-35)

mm=str(mm)

bArr="0"

while True:
    if m != 10:
        b=str(input("Number to be translated:"))
    else:
        while True:
            try:
                b=int(eval(input("Number to be translated:")))
                b=str(b)
                break
            except ValueError:
                print("Base 10 has only digits in range [0,9]")
            except NameError:
                print("Base 10 has only digits in range [0,9]")
    bArr = np.array(list(b))
    bArr = vstri(bArr)
    if b.find(" ") != -1:
        print("Number should not have spaces")
    elif np.any(vurd(bArr) != 1) and m == 1:
        break
    elif np.any(vurd(bArr) >= ord(mm)):
        print("Given number has characters that are not contained in base " + str(m))
    else:
        break

while True:
    try:
        n=int(input("Give the base of the system you want the number "+str(b)+" to be translated to: "))
        if 1<=n<=62:
            break
        else:
            print("The base musst be in range [1, 62]")
    except ValueError:
        print("Give the base number in base 10")

e=b

def g():
    if m != 10:
        x=0
        st=str(b)
        for i in range(len(str(b))):
            if m==1:
                x=x+(int(st[0]))
            else:
                try:
                    x = x + (int(st[0])*m**(len(st)-1))
                except ValueError:
                    if 64<ord(st[0])<91:
                        x=x+(ord(st[0])-64+9)*m**(len(st)-1)
                    elif 96<ord(st[0])<123:
                        x=x+(ord(st[0])-96+9+26)*m**(len(st)-1)
            st=st[1:]
            #print(st)
            #print(x)
    else:
        x=int(b)
    return (x)

a=g()

def f():
    b=a
    Out=""
    if n==1:
        for i in range(a):
            Out=Out+"1"
    else:
        c=ma.ceil(ma.log(a,n))
        for i in range(c+1):
            if np.remainder(b,n)<10:
                Out=str(np.remainder(b,n)) +Out
            elif 36>n>=10:
                Out=chr(64+(np.remainder(b,n)-9)) +Out
            elif (36+27)>n>=36:
                if (36+27)>np.remainder(b,n)>=36:
                    Out=chr(96+(np.remainder(b,n)-35)) +Out
                elif 36>np.remainder(b,n)>=10:
                    Out=chr(64+(np.remainder(b,n)-9)) +Out
            b=ma.floor(b/n)
        #print("i=",i)
        #print("b=",b)
        #print("Out=",Out)
            if b==0: 
                break
    SUB = str.maketrans("0123456789", "₀₁₂₃₄₅₆₇₈₉")

    print(e+str(str(m).translate(SUB))+"="+str(Out)+str(str(n).translate(SUB)))

f()