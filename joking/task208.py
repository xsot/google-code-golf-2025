# minor zlib improvements
def p(g):
 M=min(sum(A:=g,[]),key=sum(A:=g,[]).count);E,D=len(A:=[A for A in zip(*A)if M in A]),len(A:=[A for A in zip(*A)if M in A])
 for B,r in enumerate(g):
  for C,c in enumerate(r[:-E]):
   if(c!=M)>sum(sum(A[1+C:C+E-1])for A in g[1+B:B+D-1]):
    for g[B][C:C+E]in A:B+=1
    return g