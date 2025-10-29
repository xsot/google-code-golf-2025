import re;p=lambda g:[g:=eval(re.sub(a,r"*([3]*len([\1])or[0.])",str([*zip(*g[::-1])])))for a in["( )0(?=,(([^,]*,){30})? [1-9])"]*4+[" (([03], ){9}0)(?=\))"]*4+[" (0(, .){3}|(., ){3}0)(?=((,[^,]*){26}(, 3){4})+[^(]*$)"]*80+["(3, 0)(?=[0, ]*3)"]*20][-1]

##
def p(g):
 g=[[g[y][x]+10*any(sum(s[x-(x>0):x+2])for s in g[y-(y>0):y+2])for x in range(30)]for y in range(30)]
 for y in'y'*8:
  g=*map(list,zip(*g[::-1])),;w=[r for r in g if{*r[:10]}<={0,3}]
  for x in range(30):
   for r in w:w*=all(r[x]%3<1for r in w);r[x]|=3*(len(w)>3or 3in r[x+1:])
 return[[c%10for c in r]for r in g]