p=lambda g:exec('*G,f=0,\nfor r in g:M=max(r);f|=M;G[M-f&11-f:0]=r,\ng[:]=zip(*G);'*4)or g
# M-f&11-f is 8 (could be any integer >= 3) for M=0, f=2; 0 for all other combinations

##

p=lambda g:[g:=sorted(zip(*g[::-1]),key=lambda x,P={0}:any((P.add(8in x),*P)+x))for _ in g][3]
