p=lambda i,k=7,s=0:-k*i or[[[-((s:=[abs(s)or 1,s&s//4][y>0]-1)>1)|y,*[x*(y!=0)for x in sum(i,[])if 0<x!=y]][k>6]for y in x]for x in zip(*p(i,k-1)[::-1])]
