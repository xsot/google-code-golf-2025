def p(g):
 G=g
 for s in G*4:G=[[*s]for s in zip(*G[-5:])if{*s}-{0,4}];g=[[*s]for s in zip(*g[(4in g[-1])-2::-1])]
 for s,r in enumerate(g):
  if[1for y,r in enumerate(g)for x,r in enumerate(s*r)for Y,r in enumerate(s*G*all(g in[0,((G+32*[[]])[(Y-y)//s]+32*[4])[(X-x)//s]]for Y,g in enumerate(g)for X,g in enumerate(g)))for X,r in enumerate(s*r)for g[Y+y][X+x]in[G[Y//s][X//s]]]:return g


## experimenting with more specific zip replacing
def p(g):
 G=g
 for s in G*4:G=[[*s]for s in zip(*G[#['~4','-5']#:])if{*s}-{0,4}];g=[[*s]for s in zip(*g[(4in g[-1])-2::-1])]
 for s,r in enumerate(g):
  if[#range(7)#for y,r in enumerate(g)for x,r in enumerate(s*r)for Y,r in enumerate(s*all(g in[0,((G+#range(20,60)#*[[]])[(Y-y)//s]+#[prev_vals[-1]]#*[4])[(X-x)//s]]for Y,g in enumerate(g)for X,g in enumerate(g))*G)for X,r in enumerate(s*r)for g[Y+y][X+x]in[G[Y//s][X//s]]]:return g

## parser
totals = {}
h = {}

def zip_replace(src,target,prev_vals = []):
 if "#" in src:
    z = re.search(r"#([^#]+)#", src)[1]
    a = 0
    if z not in totals: totals[z] = {}
    for t in eval(z):
        l = zip_replace(re.sub(r"#[^#]+#", str(t), src, 1), target, prev_vals + [t])
        a += l
        if t not in totals[z]: totals[z][t] = 0
        totals[z][t] += l
    return a
 else:
    zipped_src, _ = compress(src.encode())
    if len(zipped_src) <= target:
        if len(zipped_src) not in h:
         print(len(zipped_src))
         h[len(zipped_src)] = src
         print(src)
        return 1
    return 0