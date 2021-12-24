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
        m=int(input("Anna alkuperäisen luvun luku järjestelmä:"))
        if 0<m<=62:
            break
        elif m<=0 or m>62:
            print("Järjestellmän, josta haluat muuttaa lukusi, perusluku on oltava välillä [1,62]")
    except ValueError:
        print("Anna järjestelmän perusluku kymmenluku järjestelmän lukuna")

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
        b=str(input("Muutettava luku:"))
    else:
        while True:
            try:
                b=int(eval(input("Muutettava luku:")))
                b=str(b)
                break
            except ValueError:
                print("Kymmenjärjestelmäluvussa voi vain olla numeroita")
            except NameError:
                print("Kymmenjärjestelmäluvussa voi vain olla numeroita")
    bArr = np.array(list(b))
    bArr = vstri(bArr)
    if b.find(" ") != -1:
        print("Luvussa ei voi olla välilyöntiä")
    elif np.any(vurd(bArr) != 1) and m == 1:
        break
    elif np.any(vurd(bArr) >= ord(mm)):
        print("Antamassasi luvussa on merkkejä jotka ei kuulu " + str(m) + "-lukujärjestelmään")
    else:
        break

while True:
    try:
        n=int(input("Anna luku järjestelmä johon haluat muuttaa luvun "+str(b)+": "))
        if 1<=n<=62:
            break
        else:
            print("Järjestellmän, johon haluat muuttaa lukusi, perusluku on oltava 2-62")
    except ValueError:
        print("Anna järjestelmän perusluku kymmenluku järjestelmän lukuna")

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