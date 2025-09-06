p=lambda i:[[[min(f+q,key=f.count)for*f,in zip(*s)]for q in s]for y in range(5**6)if len({*str(s:=[r[y//625:][:10-y//5%5]for r in i[y//25%25:][:10-y%5]])})<7and s[5:]][0]

##
p=lambda i,r=range(25):[[[min(f+q,key=f.count)for*f,in zip(*s)]for q in s]for y in r for x in r for a in r if len({*str(s:=[r[y:y+10-a//5]for r in i[x:x+10-a%5]])})<7and s[5:]][0]
p=eval("lambda i:[[[min(f+q,key=f.count)for*f,in zip(*s)]for q in s]"+"for %s in range(25)"*3%(*'yxa',)+"if len({*str(s:=[r[y:y+10-a//5]for r in i[x:x+10-a%5]])})<7and s[5:]][0]")