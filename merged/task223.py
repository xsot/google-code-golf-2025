# att (52 vs 51 bytes for gold)
p=lambda a:eval("[[a "+"for a in a for _ in%s]"%a*2)

### combined (tied, 52 bytes)
p=lambda a:eval("[[a "+"for a in a for _ in%s]"%a*2)

### xsot (tied, 52 bytes)
p=lambda m:eval("[[m "+"for m in m for _ in%r]"%m*2)
# p=lambda m:eval("[[m "+"for m in m for _ in[0]*3]"*2)

# same as 307 with an extra save

### ovs (59 bytes)
p=lambda g:[[j for j in i for _ in i]for i in g for _ in g]
