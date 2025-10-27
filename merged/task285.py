# compression_experiments (274 (431 unzipped) vs 262 bytes for gold)
def	p(o):
	for*i,in[[]]*8:
		o=[i[::-1]for*i,in	zip(*o)]
		for	r,m	in	enumerate(o):
			for	e,m	in	enumerate(m):
				if	m:
					n={(r,e)}
					for	t	in*i,:
						if{(r-1,e),(r,e-1),(r-1,e+1),(r-1,e-1)}&t:i.remove(t);n|=t
					i+=[n]
		for	r,m	in	enumerate(o):
			for	e,m	in	enumerate(m):
				for	t	in*i,:
					for	n,f	in	t:
						if{(n-e,f-~r),(n-~e,f-r)}&t:o[n-e][f-r]|=len({*str([i[f:f+2]for*i,in	o[n:n+2]])})//8*o[n][f]
	return	o

### joking (275 (431 unzipped) bytes)
def	p(g):
	for*I,in[[]]*8:
		g=[I[::-1]for*I,in	zip(*g)]
		for	A,r	in	enumerate(g):
			for	B,r	in	enumerate(r):
				if	r:
					E={(A,B)}
					for	G	in*I,:
						if{(A-1,B),(A,B-1),(A-1,B+1),(A-1,B-1)}&G:I.remove(G);E|=G
					I+=[E]
		for	A,r	in	enumerate(g):
			for	B,r	in	enumerate(r):
				for	G	in*I,:
					for	E,F	in	G:
						if{(E-B,F-~A),(E-~B,F-A)}&G:g[E-B][F-A]|=len({*str([I[F:F+2]for*I,in	g[E:E+2]])})//8*g[E][F]
	return	g
# would using complex numbers as coordinates do better?

##
def p(g):
 for*I,in[#['[]','()']##]*8:
  g#['[::-1]','']##=[I#[' ',' ' if '[::-1]' in prev_vals[-1:] else '[::-1]']##for*I,in zip(*g#['','' if '[::-1]' in prev_vals[-2:] else '[::-1]']##)]#['' if '[::-1]' in prev_vals[-3:] else '[::-1]']##
  for A,r in enumerate(g):
   for B,r in enumerate(r):
    if r:
     E={(A,B)}
     for G in*I,:
      if{(A-1,B),(A,B-1),(A-1,B+1),(A-1,B-1)}&G:I.remove(G);E|=G
     I+=[E]
  for A,r in enumerate(g):
   for B,r in enumerate(r):
    for G in*I,:
     for E,F in G:
      if{(E-B,F-~A),(E-~B,F-A)}&G:g[E-B][F-A]|=len({*str([I[F:F+2]for*I,in g#['[E:E+2]]','][E:E+2]']##)})//8*g[E][F]
 return g

### mwi (296 (423 unzipped) bytes)
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

### xsot (301 (426 unzipped) bytes)
def p(g):
 for E in range(8):
  I=[]
  for A,r in enumerate(g):
   for B,F in enumerate(r):
    G={(A,B)}
    for D in I[:F*5]:
     if{(A-1,B),(A,B-1),(A-1,B+1),(A-1,B-1)}&D:I.remove(D);G|=D
    I+=[G][:F]
  for G in I:
   for A,B in G:
    for E in range(8):
     for F in range(8):
      if{(A-F,B-~E),(A-~F,B-E)}&{*G}:g[A-F][B-E]|=len({*str([x[B:B+2]for x in g[A:A+2]])})//8*g[A][B]
  *g,=map(list,zip(*g[::-1]))
 return g

### ovs (308 (426 unzipped) bytes)
def p(g):
 for _ in range(8):
  I=[]
  for A,r in enumerate(g):
   for B,F in enumerate(r):
    G={(A,B)}
    for D in I[:F*5]:
     if{(A-1,B),(A,B-1),(A-1,B+1),(A-1,B-1)}&D:I.remove(D);G|=D
    I+=[G][:F]
  for G in I:
   for C,D in G:
    for E in range(5):
     for F in range(5):
      if{*G}&{(C-F,D-~E),(C-~F,D-E)}:g[C-F][D-E]|=len({*str([x[D:D+2]for x in g[C:C+2]])})//8*g[C][D]
  *g,=map(list,zip(*g[::-1]))
 return g

### combined (316 (400 unzipped) bytes)
def p(g,k=7):
 I=[]
 for A,r in enumerate(g):
  for B,F in enumerate(r):
   G={(A,B)}
   for D in(F>0)*I:
    if{(A-1,B),(A,B-1),(A-1,B+1),(A-1,B-1)}&D:I.remove(D);G|=D
   I+=(F>0)*[G]
 for G in I:
  for C,D in G:
   for E in range(25):
    if{*G}&{(C-E%5,E//5-~D),(E%5-~C,D-E//5)}:g[C-E%5][D-E//5]|=len({*str([x[D:D+2]for x in g[C:C+2]])})//8*g[C][D]
 return-k*g or p([*map(list,zip(*g[::-1]))],k-1)
