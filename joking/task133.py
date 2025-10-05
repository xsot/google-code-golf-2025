def	p(g):
	*C,M={i*66+j:g	for	i,g	in	enumerate(g)for	j,g	in	enumerate(g)if	g},
	for	A	in	M:
		G={A}
		for	D	in*C,:
			if{A-66,A-1}&D:C.remove(D);G|=D
		C+=G,
	for	A	in	C:
		for	D	in	A:
			for	G	in	A:
				for	I	in	1//sum(M[D]==M[k]for	k	in	A)*C:
					for	Q	in{G}^A:
						for	V	in(E:=[k	for	k	in	I	if	M[G]==M[D]==M[k]]):V+=(len(E)^6)%6*(Q-G);g[V//66][V%66],={M[k]for	k	in	I}-{M[D]}
	return	g


##
def p(g):
 *C,M={i*#[*range(30,100)]##+j:g for i,g in enumerate(g)for j,g in enumerate(g)if g},
 for A in M:
  G={A}
  for D in*C,:
   if{A-#[prev_vals[0]]##,A-1}&D:C.remove(D);G|=D
  C+=G,
 for A in C:
  for D in A:
   for G in A:
    for I in 1//sum(M[D]==M[k]for k in A)*C:
     for Q in{G}^A:
      for V in(E:=[k for k in I if #['M[G]==M[D]==M[k]','M[D]==M[k]==M[G]']##]):V+=(len(E)^6)%6*(Q-G);g[V//#[prev_vals[0]]##][V%#[prev_vals[0]]##],={M[k]for k in I}-{M[D]}
 return g