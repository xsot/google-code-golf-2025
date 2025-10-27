def	p(f):
	for*i,in[[]]*8:
		f=[i[::-1]for*i,in	zip(*f)]
		for	n,o	in	enumerate(f):
			for	t,o	in	enumerate(o):
				if	o:
					u={(n,t)}
					for	r	in*i,:
						if{(~-n,t),(n,~-t),(~-n,~-t),(~-n,-~t)}&r:i.remove(r);u|=r
					i+=[u]
		for	n,o	in	enumerate(f):
			for	t,o	in	enumerate(o):
				for	r	in*i,:
					for	u,e	in	r:
						if{(u-t,e-~n),(u-~t,e-n)}&r:f[u-t][e-n]|=len({*str([i[e:e+2]for*i,in	f[u:u+2]])})//8*f[u][e]
	return	f

##
def	p(g):
	for	E	in	range(8):
		I=[]
		for	A,r	in	enumerate(g):
			for	B,F	in	enumerate(r):
				G={(A,B)}
				for	D	in	I[:F*5]:
					if{(A-1,B),(A,B-1),(A-1,B+1),(A-1,B-1)}&D:I.remove(D);G|=D
				I+=[G][:F]
		for	G	in	I:
			for	A,B	in	G:
				for	E	in	range(8):
					for	F	in	range(8):
						if{(A-F,B-~E),(A-~F,B-E)}&G:g[A-F][B-E]|=len({*str([x[B:B+2]for	x	in	g[A:A+2]])})//8*g[A][B]
		*g,=map(list,zip(*g[::-1]))
	return	g

## (313/438)
def p(g):
 for E in range(8):
  *I,z={y*90+x:c for y,r in enumerate(g)for x,c in enumerate(r)if c},
  for q in z:
    G={q}
    for D in*I,:
     if{q-1,q-89,q-90,q-91}&D:I.remove(D);G|=D
    I+=G,
  for G in I:
   for q in G:
    for E in range(8):
     for F in range(8):
      if{q-F*90-~E,q-~F*90-E}&G:g[q//90-F][q%90-E]|=len({*str([x[q%90:q%90+2]for x in g[q//90:q//90+2]])})//8*g[q//90][q%90]
  *g,=map(list,zip(*g[::-1]))
 return g