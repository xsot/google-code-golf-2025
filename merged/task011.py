# att (114 bytes, gold)
p=eval("lambda a:max(a*(not'8'in'%s'%a)"+f"for*a,in[*map(zip,a,a,a{',[a[3]]*9,*[a[%d:]]*3'*2%(1,2)})][::4]"*2+')')

##
p=lambda a,b=[[5]*11]*18:sum([p(c,b[9:])for*c,in map(zip,a,a,a,b,*[a[1:]]*3,b,*[a[2:]]*3)][::4],(not'8'in'%s'%a)*a)

### ovs (160 bytes)
E=enumerate;R=0,4,8
p=lambda g:[[v*(v==5)or min([sum([r[j:j+3]for r in g[i:i+3]],[])for i in R for j in R],key=sum)[i//4*3+j//4]for j,v in E(r)]for i,r in E(g)]

### combined (160 bytes)
E=enumerate;R=0,4,8
p=lambda g:[[v*(v==5)or min([sum([r[j:j+3]for r in g[i:i+3]],[])for i in R for j in R],key=sum)[i//4*3+j//4]for j,v in E(r)]for i,r in E(g)]
