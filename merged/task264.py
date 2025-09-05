# combined (216 vs 2500 bytes for gold)
p=lambda g,R=range:[[sorted([sum([s[x:x+3]for s in g[y:y+3]],[])for y in R(len(g)-2)for x in R(len(g[0])-2)],key=lambda v:[-all(v)]+[A==5for A in v])[b"\0"[B//3*3+C//3]][B%3*3+C%3]for C in R(9)]for B in R(9)]

### ovs (237 bytes)
def p(g):
 w=len(g[0]);I=0,1,2,w,w+1,w+2,2*w,w-~w,2*w+2;O=[[*I]for _ in I];f=sum(g,[]);i=0
 for v in f:
  if v:
   P=b'@6!9<@\0'[hash((*(f[i+o]!=5for o in I),))%11]
   for o in I:O[P//9+o//w][P%9+o%w]=f[i+o];f[i+o]=0
  i+=1
 return O
