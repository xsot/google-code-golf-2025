exec(f'p=lambda i:max((-{"str(s:=[x[a:b]for x in i[c:d]]).count(%r),"*3}s){"for %s in range(11)"*4})[3]'%(*"021abcd",))

##

p=lambda i:max((-(r:=str(p:=[x[a%9:10-a//9%9]for x in i[a//81%9:10-a//729]]).count)("0"),*map(r,"21"),p)for a in range(9**4))[3]
