d=dict.fromkeys;p=lambda i:len(k:=d(i[0]))>1and[[*k]]or[[x]for x in d([*zip(*i)][0])]
p=lambda g,k=0:[[c for c,C in zip(r,r[1:]+(0,))if c^C]for r in zip(*k*g or p(g,1))]