# att (63 bytes, gold)
p=lambda a:[*zip(*[iter(sum(sum(a,[]))//8*[1,0]+[0]*7)]*3)][:3]

### xsot (64 bytes)
p=lambda m:[[1,0,(c:=sum(sum(m,[]))/8)>1],[0,c>2,0],[c>3,0,c>4]]

# p=lambda m:[[1,0,(c:=str(m).count('2')/4)>1],[0,c>2,0],[c>3,0,c>4]]

### combined (64 bytes)
p=lambda m:[[1,0,(c:=sum(sum(m,[]))/8)>1],[0,c>2,0],[c>3,0,c>4]]

### ovs (65 bytes)
p=lambda g:[(w:=sum(sum(g,[]))//8*[1,0]+[0]*9)[:3],w[3:6],w[6:9]]
