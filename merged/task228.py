# joking (122 vs 120 bytes for gold)
import re
p=lambda a,n=-3:n*a or[*zip(*eval(re.sub(r'0(.{34}([^0]).*)(.)(?=, \2.*0, \2)',r'\3\1 0',str(p(a,n+1)[::-1]))))]

##
p=lambda a,n=-3:n*a or[*zip(*eval(re.sub(r'(?<=([1-9]), )((?!0|\1).)(.*\1.{34})0',r'0\3\2',str(p(a,n+1)[::-1]))))]
p=lambda a,n=-3:n*a or[*zip(*eval(re.sub(r'0(.{34}([^0]).*(?!\2|0))(\d), \2',r'\3\1 0,\2',str(p(a,n+1)[::-1]))))]

### att (148 bytes)
import re
p=lambda a,n=-3:n*a or[*zip(*eval(re.sub(f'(?<={(b:=max(sum(a,[]),key=bool))}, )([^0{b}])(.*{b}.{{34}})0',r'0\2\1',str(p(a,n+1)[::-1]))))]

### combined (189 bytes)
f=lambda A:[i for i,r in enumerate(A)if any(r)]
def p(A):
 _,E,*_,k,_=f(A);W,*_,p=f(zip(*A))
 for l,a in[[W+1,p+1],[p-1,W-1]]:A[k+2][a]=A[E][l];A[E-2][a]=A[k][l];A[E][l]=A[k][l]=0
 return A
