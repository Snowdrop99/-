import sys

def lingxingPrint(n):
    b = []
    if n%2 == 0:
        return []
    mid = int(n/2+1)
    for i in range(1,mid+1):
        c = [str(j) for j in range(1,i+1)]
        c1 = c[::-1]
        c2 = c+c1[1:]
        s = ''.join(c2)
        a = ['*'*(abs(i-mid)%mid),s,'*'*(abs(i-mid)%mid)]
        s1 = ''.join(a)
        b.append(s1)
    b1 = b[::-1]
    b2 = b+b1[1:]
    b3 = '"'+'|'.join(b2)+'"'
    return b3

n = int(input())
print(lingxingPrint(n))