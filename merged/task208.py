# xsot (223 (291 unzipped) vs 215 bytes for gold)
# random bullshit go
def p(g):
 M=min(sum(A:=g,[]),key=sum(A:=g,[]).count);E=len(A:=[A for A in zip(*A)if M in A])
 D=len(A:=[A for A in zip(*A)if M in A])
 for B,r in enumerate(g):
  for C,c in enumerate(r[:-E]):
   if(c!=M)>sum(sum(A[1+C:C+E-1])for A in g[B+1:B+D-1]):
    for g[B][C:C+E]in A:B+=1
    return g

### joking (tied, 223 (292 unzipped) bytes)
# minor zlib improvements?
def p(g):
 M=min(sum(A:=g,[]),key=sum(A:=g,[]).count)
 E=len(A:=[A for A in zip(*A)if M in A])
 D=len(A:=[A for A in zip(*A)if M in A])
 for B,r in enumerate(g):
  for C,r in enumerate(r[:-E]):
   if(r!=M)>sum(sum(A[1+C:C+E-1])for A in g[B+1:B+D-1]):
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

##

def p(g):
 e=enumerate;A=g;E,D=[len(A:=[A for*A,in zip(*A)if min(map(sum(g,[]).count,A))<25])-1for _ in'in']
 for B,r in e(g[:~D]):
  for C,c in e(r[:~E]):
   for r,r[C:C-~E]in zip(g[B+19*sum(sum(A[C+1:C+E])for A in g[B+1:B+D]):],A):0
 return g

### combined (255 (290 unzipped) bytes)
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
