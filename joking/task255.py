# based on mwi's sol
import re;p=lambda g,k=15:-k*g or p(eval(re.sub(*[["\((%s|(0, )+3, 3, 3),?"%re.search(r"([ ,03]{61,})(.*\1){3}|$",g:=str([*zip(*g[::-1])]))[1],r"(*[3]*len([\1]),"],["(?=0((,[^,]*){31}|, )[1-9])","1<"]][k>9],g)),k-1)

##
def p(g):
 for y in range(32):g=[[g[y][~x]+13*any({*r[-2%(30-x):31-x]}-{0,3}for r in g[y-1:y+2])for y in range(30)]for x in range(30)];g=[[r[x]%13|3*(len(w:=[r[x]for r in g if{*r[:10]}<={0,3}])>3!={*r[:10]}<={0,3}>={*w}or 3in r[x:]!={*r[:10]}<={0,3})for x in range(30)]for r in g]
 return g

def p(g):
 for y in range(#[*range(32,40,4)]##):g=[[g[y][~x]+#[*range(10,50)]##*any({*r[-2%(30-x):31-x]}-{0,3}for r in g[y-1:y+2])for y in range(30)]for x in range(30)];g=[[r[x]%#[prev_vals[-1]]##|3*(len(w:=[r[x]for r in g if{*r[:10]}<={0,3}])>3!={*r[:10]}<={0,3}>={*w}or 3in r[x:]!={*r[:10]}<={0,3})for x in range(30)]for r in g]
 return g