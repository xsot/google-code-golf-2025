# xsot (64 bytes, gold)
p=lambda m:[[1,0,(c:=sum(sum(m,[]))/8)>1],[0,c>2,0],[c>3,0,c>4]]

# p=lambda m:[[1,0,(c:=str(m).count('2')/4)>1],[0,c>2,0],[c>3,0,c>4]]

### combined (tied, 64 bytes)
p=lambda m:[[1,0,(c:=sum(sum(m,[]))/8)>1],[0,c>2,0],[c>3,0,c>4]]

### ovs (65 bytes)
p=lambda g:[(w:=sum(sum(g,[]))//8*[1,0]+[0]*9)[:3],w[3:6],w[6:9]]

### att (72 bytes)
p=lambda a,i=0:[[4*i<(i:=i+1)%2*s(s(a,[]))for _ in[0]*3]for s in[sum]*3]
