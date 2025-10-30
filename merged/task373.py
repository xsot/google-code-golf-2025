# xsot (38 bytes, gold)
p=lambda m:[l:=min(zip(*m))*3,l[::-1]]

### att (39 bytes)
p=lambda a:[b:=[*map(max,a)]*3,b[::-1]]

### combined (39 bytes)
p=lambda a:[b:=[*map(max,a)]*3,b[::-1]]

### ovs (42 bytes)
p=lambda g:[r:=[*[*zip(*g)][0]]*3,r[::-1]]
