f=lambda A:[i for i,r in enumerate(A)if any(r)]
def p(A):
 _,E,*_,k,_=f(A);W,*_,p=f(zip(*A))
 for l,a in[[W+1,p+1],[p-1,W-1]]:A[k+2][a]=A[E][l];A[E-2][a]=A[k][l];A[E][l]=A[k][l]=0
 return A