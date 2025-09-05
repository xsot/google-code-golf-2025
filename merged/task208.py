# joking (225 (290 unzipped) bytes, gold)
# minor zlib improvements
def p(g):
 M=min(sum(A:=g,[]),key=sum(A:=g,[]).count);E,D=len(A:=[A for A in zip(*A)if M in A]),len(A:=[A for A in zip(*A)if M in A])
 for B,r in enumerate(g):
  for C,c in enumerate(r[:-E]):
   if(c!=M)>sum(sum(A[1+C:C+E-1])for A in g[1+B:B+D-1]):
    for g[B][C:C+E]in A:B+=1
    return g

### ovs (229 (278 unzipped) bytes)
# compression abuse :)
def p(g):
 e=enumerate;M=min(k:=sum(A:=g,[]),key=k.count);E,D=len(A:=[A for*A,in zip(*A)if M in A]),len(A:=[A for*A,in zip(*A)if M in A])
 for B,r in e(g):
  for C,c in e(r[:-E]):
   if(c!=M)>sum(sum(A[C+1:C+E-1])for A in g[B+1:B+D-1]):
    for g[B][C:C+E]in A:B+=1
    return g

### combined (256 (290 unzipped) bytes)
def p(g):
 e=enumerate;A=g
 for G in'  ':A=[[*A]for A in zip(*A)if min(k:=sum(g,[]),key=k.count)in A];D,E=len(A),len(A[0])
 for B,r in e(g):
  for C,c in e(r[:-E]):
   if c!=A[0][0]!=sum(sum(A[C+1:C+E-1])for A in g[B+1:B+D-1])<1:return g[:B]+[f[:C]+F+f[C+E:]for F,f in zip(A,g[B:])]+g[B+D:]

### mwi (256 (294 unzipped) bytes)
def p(g):
 A=g
 for G in'zi':A=[[*A]for A in zip(*A)if min(k:=sum(g,[]),key=k.count)in A];D,E=len(A),len(A[0])
 for B,r in enumerate(g):
  for C,c in enumerate(r[:-E]):
   if c!=A[0][0]!=sum(sum(A[C+1:C+E-1])for A in g[B+1:B+D-1])<1:return g[:B]+[f[:C]+F+f[C+E:]for F,f in zip(A,g[B:])]+g[B+D:]
