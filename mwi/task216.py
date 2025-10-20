# exact copy of ovs/task365.py, just changed grid size
# way slower though, grid is 20x20 instead of 10x10

# 119 bytes, approx 15 minutes
exec(f'p=lambda i:max((-{"str(s:=[x[a:b]for x in i[c:d]]).count(%r),"*3}s){"for %s in range(21)"*4})[3]'%(*"021abcd",))

## 121 bytes, approx 8 minutes
exec(f'p=lambda i:max((-{"sum(s:=[x[a:b]for x in i[c:d]],s).count(%s),"*3}s){"for %s in range(21)"*4})[3]'%(*"021abcd",))