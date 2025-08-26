p=lambda g,k=-1:g*k or p([y for*y,in zip(*g)if g!=(g:=y)],k+1)

### xsot (79 bytes)
p=lambda m,i=1:-i*m or p([*zip(*m[:1]+[y for x,y in zip(m,m[1:])if x!=y])],i-1)
