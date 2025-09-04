E=enumerate
p=lambda m,X=8:[*[[[min(a:=sum(m,[]),key=a.count)*(e>0)for e in e[x:x+X]]for e in m[y:]if(f:=f*e[x]==b)]for y,r in E(m)for x,b in E(r)if(f:=[b]*X==r[x:x+X])*b],0][0]or p(m,X-1)

# instead of counting active pixels, or even calculating area, this just returns the widest possible rectangle
