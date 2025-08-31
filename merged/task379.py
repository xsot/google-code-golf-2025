# xsot (141 bytes, gold)
import re
p=lambda i,k=7,r=re.sub:-k*i or[*zip(*eval(r(", 4, ","|8,8,8|",r("0, 8, ((0, )+)2","4,2,4,*[2]*len([\\1])",str(p(i,k-1)[::-1])))))]

##
def p(m,R=range):
 f=lambda m:[*map(list,zip(*m))];a=sum(m:=[f(m),m][t:=8 in m[0]],[]);n=len(m[0])
 for i in R(n*len(m)):
  def g(*a):
   for e in R(*a):
    if m[r][e]>7:
     for j in R(min(c,e),max(c,e)+1):m[r][j]=2
     for i in b' @`!a"Bb':m[r+i//32-2][e+i%4-1]=8
     break
  r=i//n;a[i]==2!=g(c:=i%n,0,-1)!=g(c+1,n)
 return[f(m),m][t]

#####
# Write a python function that takes a list of list of digits (0/2/8) representing a matrix.
# This matrix contains at most 2 rows made up of 8s and some single cells containing 2.
# For each 2, draw a vertical line of 2s moving it towards each 8 row, overwriting the value
# at the intersection point with a 2. If a row is behind another row, stop at the first
# intersection. At each intersection, replace all 8 neighbouring cells with 2s. The logic
# should be as concise and simple as possible.
def p(m):
    f=lambda m:[*map(list,zip(*m))]
    t=8 in m[0]
    m = m if t else f(m)
    rows, cols = len(m), len(m[0])

    a=sum(m,[])
    for i in range(rows*cols):
        if a[i] != 2:
            continue
        r = i//cols
        c = i%cols
        def splash(a):
            for e in a:
                if m[r][e] == 8:
                    for j in range(min(c,e),max(c,e) + 1):
                        m[r][j] = 2
                    for dr in [-1,0,1]:
                        for dc in [-1,0,1]:
                            if dr|dc:m[r+dr][e+dc] = 8
                    break
        splash(range(c, 0, -1))
        splash(range(c + 1, cols))

    return m if t else f(m)
