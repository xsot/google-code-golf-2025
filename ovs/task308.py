def p(g,**Q):
 for N in sum(g,[]):C=[C+A*32for A,g in enumerate(g)for C,g in enumerate(g)if g==N];Q|={J+99-sum(C)//4:N for J in C if len(C)<5}
 return[[Q.get(C+A*32,*{*g[0]}&{*g[5]})for C in range(min(Q)>>5,max(Q)//32+1)]for A in range(min(Q)>>5,max(Q)//32+1)]

## this can probably use some more compression optimization. Best uncompressed I have is 232:
e=enumerate
def p(g,**A):
 for N in sum(g,[]):C=[C+A*16for(A,B)in e(g)for(C,E)in e(B)if E==N];A|={J+51-sum(C)//4:N for J in C if len(C)<5}
 q=range(min(A)>>4,max(A)//16+1);return[[A.get(y*16+x,*{*g[0]}&{*g[5]})for x in q]for y in q]
