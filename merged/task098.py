# joking (64 bytes, gold)
p=lambda i,*w:i*0!=0and[*map(p,i,i[:1]+i,i[1:]+i,*w)]or i^min(w)

##
p=lambda i:[[y^min(t)for*t,y in zip(*w,[0]+s,s[1:]+[0],s)]for*w,s in zip(i[:1]+i,i[1:]+i,i)]

### ovs (101 bytes)
E=enumerate
p=lambda g:[[v*(0in[*r[j-1:j+2],*[*zip(*g)][j][i-1:i+2]])for j,v in E(r)]for i,r in E(g)]

### combined (101 bytes)
E=enumerate
p=lambda g:[[v*(0in[*r[j-1:j+2],*[*zip(*g)][j][i-1:i+2]])for j,v in E(r)]for i,r in E(g)]
