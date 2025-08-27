p=eval(f"lambda a:max([str(a).count('1'),a]{'for*a,in map(zip,a,a[1:],a[2:])'*2})[1]")

### ovs (94 bytes)
p=lambda g:max((str(x:=[r[i//7:][:3]for r in g[i%7:][:3]]).count('1'),x)for i in range(49))[1]
