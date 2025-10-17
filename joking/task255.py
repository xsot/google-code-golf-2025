def p(g):
 for y in range(32):g=[[g[y][~x]+13*any({*r[-2%(30-x):31-x]}-{0,3}for r in g[y-1:y+2])for y in range(30)]for x in range(30)];g=[[r[x]%13|3*(len(w:=[r[x]for r in g if{*r[:10]}<={0,3}])>3!={*r[:10]}<={0,3}>={*w}or 3in r[x:]!={*r[:10]}<={0,3})for x in range(30)]for r in g]
 return g

##
def p(g):
 for y in range(#[*range(32,40,4)]##):g=[[g[y][~x]+#[*range(10,50)]##*any({*r[-2%(30-x):31-x]}-{0,3}for r in g[y-1:y+2])for y in range(30)]for x in range(30)];g=[[r[x]%#[prev_vals[-1]]##|3*(len(w:=[r[x]for r in g if{*r[:10]}<={0,3}])>3!={*r[:10]}<={0,3}>={*w}or 3in r[x:]!={*r[:10]}<={0,3})for x in range(30)]for r in g]
 return g