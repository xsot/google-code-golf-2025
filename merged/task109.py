# att (91 vs 81 bytes for gold)
p=lambda a:[*map(f:=lambda*b,i=len(a)//2:[c and b[i]for c in b[:i]+b[i-1::-1]],*map(f,*a))]
