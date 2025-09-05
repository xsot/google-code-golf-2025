# ovs (91 vs 86 bytes for gold)
p=lambda m,x=1,d=-1:m and p(m,x:=x+d,x%(l:=len(m.pop())-1)and d or-d)+[[8]*x+[1]+[8]*(l-x)]

### xsot (92 bytes)
p=lambda m,x=1,d=-1:m and p(m[1:],x:=x+d,x%(l:=len(m[0])-1)and d or-d)+[[8]*x+[1]+[8]*(l-x)]

##
p=lambda m,x=1,d=-1:m and p(m[1:],x:=x+d,x%(l:=len(m[0])-1)and d or-d)+[[8]*x+[1]+[8]*(l-x)]
p=lambda m,x=1,d=-1:m and p(m[1:],x:=x+d,d*2*(x%(l:=len(m[0])-1)>0)-d)+[[8]*x+[1]+[8]*(l-x)]
p=lambda m,x=1,d=-1:m and p(m[1:],x:=x+d,d*2*((l:=len(m[0])-1)>x>0)-d)+[[8]*x+[1]+[8]*(l-x)]

p=lambda m,x=1,d=-1:m and(l:=len(m[0])-1)and p(m[1:],x:=x+d,d*2*(0<x<l)-d)+[[8]*x+[1]+[8]*(l-x)]

p=lambda m,d=1,x=0:m and(l:=len(m[0]))and p(m[1:],d:=d*2*(0<=x+d<l)-d,x+d)+[[8]*x+[1]+[8]*(l+~x)]

p=lambda m,d=1,c=0:m and p(m[1:],d:=d*(~-(0<=c+d<len(m[0]))|1),c+d)+[[8]*c+[1]+[8]*(len(m[0])+~c)]

p=lambda m:exec("r-=1;m[r][~abs(~r%(2*~-N)-N+1)]=1;"*len(m:=[[8]*(N:=len(m[r:=0]))for _ in m]))or m

###
p=lambda m,r=0:exec("r-=1;m[r][~abs(~r%(2*~-N)-N+1)]=1;"*len(m:=[[8]*(N:=len(m[0]))for _ in m]))or m
# compute directly instead of tracing
def p(m):r=len(m);m=[[8]*(N:=len(m[0]))for _ in m];exec("m[-r][~abs((r-1)%(2*~-N)-N+1)]=1;r-=1;"*r);return m


p=lambda m,r=0,c=0,d=1:exec("r-=1;m[r]=[8]*c+[1]+[8]*((n:=len(m[0]))+~c);d*=~-(0<=c+d<n)|1;c+=d;"*len(m))or m
def p(m):r=c=0;d=1;exec("r-=1;m[r]=[8]*c+[1]+[8]*((n:=len(m[0]))+~c);d*=~-(0<=c+d<n)|1;c+=d;"*len(m));return m

p=lambda m,d=1,r=0,c=0:exec("r-=1;m[r][c]=1;d*=~-(0<=c+d<len(m[0]))|1;c+=d;"*len(m))or eval(str(m).replace(*'08'))
def p(m):m=[[8]*(n:=len(m[0]))for _ in m];r=c=0;d=1;exec("r-=1;m[r][c]=1;d*=~-(0<=c+d<n)|1;c+=d;"*len(m));return m

# trace path
def p(m):
 m=[[8]*(n:=len(m[0]))for _ in m];r,c,d=len(m),0,1
 while r:r-=1;m[r][c]=1;d*=~-(0<=c+d<n)|1;c+=d
 return m

### combined (92 bytes)
p=lambda m,x=1,d=-1:m and p(m[1:],x:=x+d,x%(l:=len(m[0])-1)and d or-d)+[[8]*x+[1]+[8]*(l-x)]
