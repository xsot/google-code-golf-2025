def p(a):
 m,*a=a;m+=(4-m.count(0))*5*[0]
 for _ in m:a=[m]+a;m=[0]+m[:-1]
 return a

##
def p(a):
 m=a.pop();m+=(4-m.count(0))*5*[0]
 for _ in m:a=[m]+a;m=[0]+m[:-1]
 return a