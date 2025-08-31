# combined (63 bytes, gold)
p=lambda m:[*zip(sorted({*(a:=sum(m,[]))},key=a.count))][2::-1]

### xsot (tied, 63 bytes)
p=lambda m:[*zip(sorted({*(a:=sum(m,[]))},key=a.count))][2::-1]
# same as task393 (f8ff0b80)

### att (69 bytes)
p=lambda a:[[sorted(range(10),key=sum(a,a).count)[i]]for i in(7,6,5)]

### ovs (71 bytes)
p=lambda g:[[int(v)]for v in sorted({*str(g)},key=str(g).count)[2::-1]]
