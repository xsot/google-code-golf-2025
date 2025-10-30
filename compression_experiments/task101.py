def p(e):
 i,r,o,u,n=[{a+m*20for m,e in enumerate(e)for a,e in enumerate(e)if e==f}for f in range(5)]
 for f in o:u|={f for f in o for m in r|u if abs(f-m)in(1,20)}
 for f in o:b={f}-n and{f-min(len({f+m*(s-2)for s in range(5)}&o)for m in(1,20))*(min(u)-max(u))}&o;n|=b;e=[[e or a+m*20in(b and{f-min(len({f+m*(s-2)for s in range(5)}&o)for m in(1,20))*(min(u)-m)for m in r})for a,e in enumerate(e)]for m,e in enumerate(e)]
 return e