# ovs (207 vs 199 bytes for gold)
def p(g):j=D=0;P=[];exec("for r in g:F=r[j]==4;P+=[r[j]]*D;D^=F;r[j]*=D|F<1\nj+=1\n"*13+"g[:]=filter(any,zip(*g));"*2);A,*_,B=map(max,*g);E=4,*[0]*len(g[0]),4;return[E,*[[A,*r,B][::A==P[0]or-1]for r in g],E]

### mwi (248 (312 unzipped) bytes)
def p(g):
 H,I=divmod(sum(p:=g,[]).index(4),len(g))
 for A in' zip':x=();p=[[*A][::-1]for A in zip(*p)if 4in(x:=x+A)]
 for(C,D)in enumerate(p):g[C+H][I:I+len(D)]=[0]*len(D)
 for A in' zip':x=();s=g;g=[A[::-1]for A in zip(*g)if sum(x:=x+A)]
 for(C,D)in enumerate(g):p[C+1][1:-1]=D[::1|-(p[1][0]in s[0])]
 return p

### combined (251 (306 unzipped) bytes)
def p(g):
 B=enumerate;H,I=divmod(sum(p:=g,[]).index(4),len(g))
 for _ in'_'*4:x=();p=[[*A][::-1]for A in zip(*p)if 4in(x:=x+A)]
 for(C,D)in B(p):g[C+H][I:I+len(D)]=[0]*len(D)
 for _ in'_'*4:x=();s=g;g=[A[::-1]for A in zip(*g)if sum(x:=x+A)]
 for(C,D)in B(g):p[C+1][1:-1]=D[::1|-(p[1][0]in s[0])]
 return p
