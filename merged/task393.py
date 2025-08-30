# xsot (63 bytes, gold)
p=lambda m:[*zip(sorted(set(a:=sum(m,[])),key=a.count))][2::-1]
# p=lambda m:[*map(list,zip(sorted(set(a:=sum(m,[]))-{0},key=a.count)))][::-1]
# p=lambda m:(a:=sum(m,[]))and[[e]for e in sorted(set(a)-{0},key=a.count)][::-1]

### att (69 bytes)
p=lambda a:[[sorted(range(10),key=sum(a,a).count)[i]]for i in(8,7,6)]

### ovs (72 bytes)
def p(g):f=sum(g,[]);return[[v]for v in sorted({*f},key=f.count)[2::-1]]

### combined (73 bytes)
p=lambda i:[[x]for x in sorted({*sum(i,[])},key=sum(i,[]).count)[-2::-1]]
