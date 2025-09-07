def p(a,i=-1):
 for i in(I:={i//10+i:v*(v!=8)for v in sum(a,[])if[i:=i+1]*v}):s={i};[s.add(y)for y in[*I]*6if{y+1,y-1,y+11,y-11}&s];a[i//11][i%11]=I[[s for s in I if I[s]][sorted(s).index(i)]]-I[i]
 return a