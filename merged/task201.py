# combined (306 vs 217 bytes for gold)
def p(g):
 B=enumerate;H,I=divmod(sum(p:=g,[]).index(4),len(g))
 for _ in'_'*4:x=();p=[[*A][::-1]for A in zip(*p)if 4in(x:=x+A)]
 for(C,D)in B(p):g[C+H][I:I+len(D)]=[0]*len(D)
 for _ in'_'*4:x=();s=g;g=[A[::-1]for A in zip(*g)if sum(x:=x+A)]
 for(C,D)in B(g):p[C+1][1:-1]=D[::1|-(p[1][0]in s[0])]
 return p
