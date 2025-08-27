r=lambda g:[r[::-1]for*r,in zip(*g)]
def p(g):u=*map(set,g),{0,8};j=u.index(max(u,key=len));i=u.index({0,8});return g[:i]==i*g[:1]and g[:i]+[g[j-1]]+[g[j]]*(j+~i)+g[j:]or r(r(r(p(r(g)))))