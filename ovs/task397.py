p=lambda m,k=80:exec('r=k//9-1;exec("%s=3,3;"*len(a:={*%s+%s})*all(a));k-=1;'%(('m[r:=r+1][k%9:k%9+2]',)*3)*81)or m
