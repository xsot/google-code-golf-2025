def p(g):
 H,I=divmod(sum(p:=g,[]).index(4),len(g))
 for A in' zip':x=();p=[[*A][::-1]for A in zip(*p)if 4in(x:=x+A)]
 for(C,D)in enumerate(p):g[C+H][I:I+len(D)]=[0]*len(D)
 for A in' zip':x=();s=g;g=[A[::-1]for A in zip(*g)if sum(x:=x+A)]
 for(C,D)in enumerate(g):p[C+1][1:-1]=D[::1|-(p[1][0]in s[0])]
 return p