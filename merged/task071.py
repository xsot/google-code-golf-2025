# mwi (195 vs 119 bytes for gold)
def p(g,k=0):C=[*{}.fromkeys(sum(g,[]))][1];e=[[C*(c and C in((r+[0]*99)[k-k%2*2-x],c))for x,c in enumerate(r)]for r in g];return e*all(z[k//2-5:k//2]==z[k//2+1-k%2:][4::-1]for z in e)or p(g,k+1)

### combined (235 (247 unzipped) bytes)
p=lambda i,n=11,s=0,l=-1:all(len({*c,l})<3for x in i for c in zip(x[n:],x[n-s::-1]))and[[[y,*x[2*n-b-s:]][y==l]for b,y in enumerate(x)]for x in i]or p(i,n-s,1-s,max(sum(i,[]),key=lambda q:{q,0}>{c[0]for x in i for c in zip(x,*i)if q in{*x}&{*c}}))
