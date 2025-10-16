def p(g):
 M=min(sum(A:=g,[]),key=sum(A:=g,[]).count);E=len(A:=[A for A in zip(*A)if M in A])
 D=len(A:=[A for A in zip(*A)if M in A])
 for C in range(22-E):
  for B in range(22-D):
   for g[B][C:C+E]in A*0**sum(sum(A[C:C+E][1:-1])for A in g[B:B+D][1:-1]):B+=1
 return g