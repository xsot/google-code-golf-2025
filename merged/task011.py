# att (125 vs 121 bytes for gold)
v=[[5]*11]*9
p=eval(f"lambda a:[a {'for*a,in map(zip,a,a,a,v,*[a[1:]]*3,v,*[a[2:]]*3)'*2}if(c:=sum(a,()).count)(5)<c(0)][0]")

### ovs (160 bytes)
E=enumerate;R=0,4,8
p=lambda g:[[v*(v==5)or min([sum([r[j:j+3]for r in g[i:i+3]],[])for i in R for j in R],key=sum)[i//4*3+j//4]for j,v in E(r)]for i,r in E(g)]

### combined (160 bytes)
E=enumerate;R=0,4,8
p=lambda g:[[v*(v==5)or min([sum([r[j:j+3]for r in g[i:i+3]],[])for i in R for j in R],key=sum)[i//4*3+j//4]for j,v in E(r)]for i,r in E(g)]
