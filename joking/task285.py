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