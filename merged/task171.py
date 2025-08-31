# att (54 bytes, gold)
p=lambda a:[*map(f:=lambda*b:[8,*b[2:],8],*map(f,*a))]

### combined (tied, 54 bytes)
p=lambda a:[*map(f:=lambda*b:[8,*b[2:],8],*map(f,*a))]

### ovs (61 bytes)
p=lambda g,k=-1:g*k or p([[8,*r,8]for _,*r,_ in zip(*g)],k+1)

### xsot (66 bytes)
p=lambda m:[[8,*[x]*(len(m[0])-2),8]for x in[8,*[0]*(len(m)-2),8]]

##
p=lambda m:[[8,*[x]*(len(m[0])-2),8]for x in[8,*[0]*(len(m)-2),8]]
p=lambda m:(r:=[[8]*len(x:=m[0])])+[[8,*[0]*(len(x)-2),8]]*(len(m)-2)+r
p=lambda m,i=3:-i*m or p([*map(list,zip(*([[8]*len(m[0])]+m[1:])[::-1]))],i-1)
