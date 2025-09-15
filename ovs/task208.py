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
