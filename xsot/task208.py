# random bullshit go
def p(g):
 M=min(sum(A:=g,[]),key=sum(A:=g,[]).count);E=len(A:=[A for A in zip(*A)if M in A])
 D=len(A:=[A for A in zip(*A)if M in A])
 for B,r in enumerate(g):
  for C,c in enumerate(r[:-E]):
   if(c!=M)>sum(sum(A[1+C:C+E-1])for A in g[B+1:B+D-1]):
    for g[B][C:C+E]in A:B+=1
    return g
