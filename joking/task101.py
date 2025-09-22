# zip optimising
def p(g):
 V,m,M,s,v=[{j+i*20for i,g in enumerate(g)for j,g in enumerate(g)if g==I}for I in range(5)];[s.add(I)for I in[*M]*2for i in m|s if abs(I-i)in[1,20]]
 for i in M-s:
  j={i}-v and{i-min(len({*range(i-2*I,i+3*I,I)}&M)for I in[1,20])*(min(s)-max(s))}&M;v|=j
  for I in j and{i-min(len({*range(i-2*I,i+3*I,I)}&M)for I in[1,20])*(min(s)-I)for I in m}&V:g[I//20][I%20]=1
 return g