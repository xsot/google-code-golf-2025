p=lambda m:eval("[[m "+"for m in m for _ in%r]"%m*2)
# p=lambda m:eval("[[m "+"for m in m for _ in[0]*3]"*2)

# same as 307 with an extra save

### ovs (59 bytes)
p=lambda g:[[j for j in i for _ in i]for i in g for _ in g]
