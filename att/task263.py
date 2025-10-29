p=lambda g:g[(T:=[*zip(*[map(bool,sum(g,g*0))]*9)]).index(min(T,key=T.count))*3:][:3%len(g)]or[*zip(*p((*zip(*g),)))]

##
s='for*a,in map(zip,*[iter(a)]*3)'*2;p=eval(f"lambda a:[a {s}][(b:=[str(a).count('0'){s}]).index(min(b,key=b.count))]")
