p=lambda m:[*zip(sorted(set(a:=sum(m,[])),key=a.count))][2::-1]
# p=lambda m:[*map(list,zip(sorted(set(a:=sum(m,[]))-{0},key=a.count)))][::-1]
# p=lambda m:(a:=sum(m,[]))and[[e]for e in sorted(set(a)-{0},key=a.count)][::-1]

### ovs (72 bytes)
def p(g):f=sum(g,[]);return[[v]for v in sorted({*f},key=f.count)[2::-1]]
