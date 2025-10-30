# mwi (221 bytes, gold)
import re;p=lambda g,k=15:-k*g or p(eval(re.sub(*[["\((%s|(0, )+3, 3, 3),?"%(re.search(r"([ ,03]{61,})(.*\1){3}",g:=str([*zip(*g[::-1])]))or"__")[1],r"(*[3]*len([\1]),"],["(?=0((,[^,]*){31}|, )[1-9])","-."]][k>9],g)),k-1)

##
import re;p=lambda g:[g:=eval(re.sub(a,r"*([3]*len([\1])or[0.])",str([*zip(*g[::-1])])))for a in["( )0(?=,(([^,]*,){30})? [1-9])"]*4+[" (([03], ){9}0)(?=\))"]*4+[" (0(, .){3}|(., ){3}0)(?=((,[^,]*){26}(, 3){4})+[^(]*$)"]*80+["(3, 0)(?=[0, ]*3)"]*20][-1]

##
def p(g):
 g=[[g[y][x]+10*any(sum(s[x-(x>0):x+2])for s in g[y-(y>0):y+2])for x in range(30)]for y in range(30)]
 for y in'y'*8:
  g=*map(list,zip(*g[::-1])),;w=[r for r in g if{*r[:10]}<={0,3}]
  for x in range(30):
   for r in w:w*=all(r[x]%3<1for r in w);r[x]|=3*(len(w)>3or 3in r[x+1:])
 return[[c%10for c in r]for r in g]

##

import re;p=lambda g,k=19:-k*g or p(eval(re.sub(["(3, 3, 3(, 0)+(?=\))|3(, 0)+, 3),?","((?<=\()%s),?"%(re.search(r"(0(, 0){20,})(?=(.*\1){3})",g:=str([*zip(*g[::-1])]))or"_")[0],"() 0(?=((,[^,]*){31}|, )[1-9]),"][k//7],"*([3]*len([\\1])or[-.0]),",g)),k-1)

# versions that fail a few cases
import re;p=lambda g:[g:=eval(re.sub(a,r"*([3]*len([\1])or[0.]),",str([*zip(*g[::-1])])))for a in["() 0(?=((,[^,]*){31}|, )[1-9]),"]*8+[r"(?=(?=(( 0,){4,}))(?:(?=\1)([^,]*,){30}){9,}[^(]*$)\1"]*8+["(3, 3, 3(, [03])+)(?=\))"]*8][-1]
import re;p=lambda g,k=(32*3-1):-k*g or p(eval(re.sub(["(3, 3, 3(, [03])+)(?=\))",r"(?=(?=(( 0,){%d}))(?:(?=\1)([^,]*,){30}){9,}[^(]*$)\1"%(k//4-5),"() 0(?=((,[^,]*){31}|, )[1-9]),"][k//32],r"*([3]*len([\1])or[0.]),",str([*zip(*g[::-1])]))),k-1)



## variants of new idea
import re;p=lambda g,k=19:-k*g or p(eval(re.sub(["(3, 3, 3(, 0)+(?=\))),?","((?<=\()%s),?"%(re.search(r"([03](, [03]){20,})(?=(.*\1){3})",g:=str([*zip(*g[::-1])]))or"_")[0],"() 0(?=((,[^,]*){31}|, )[1-9]),"][k//7],"*([3]*len([\\1])or[-.0]),",g)),k-1)
import re;p=lambda g,k=19:-k*g or p(eval(re.sub(["(3, 3, 3(, 0){6,}),?","((?<=\()%s),?"%(re.search(r"(0(, [03]){20,})(?=(.*\1){3})",g:=str([*zip(*g[::-1])]))or"_")[0],"() 0(?=((,[^,]*){31}|, )[1-9]),"][k//7],"*([3]*len([\\1])or[-.0]),",g)),k-1)
import re;p=lambda g,k=19:-k*g or p(eval(re.sub(["(3, 3, 3(, 0)+(?=\)))","((?<=\()%s),?"%(re.search(r"(0(, [03]){20,})(?=(.*\1){3})",g:=str([*zip(*g[::-1])]))or"_")[0],"() 0(?=((,[^,]*){31}|, )[1-9]),"][k//7],"*([3]*len([\\1])or[-.0]),",g)),k-1)
import re;p=lambda g,k=15:-k*g or p(eval(re.sub(["(?<=\()(%s|(0, )+3, 3, 3),?"%(re.search(r"(0(, [03]){20,})(?=(.*\1){3})",g:=str([*zip(*g[::-1])]))or"_")[0],"() 0(?=((,[^,]*){31}|, )[1-9]),"][k>9],"*([3]*len([\\1])or[-.0]),",g)),k-1)
import re;p=lambda g,k=15:-k*g or p(eval(re.sub(["(?<=\()(%s|(0, )+3, 3, 3),?"%(re.search(r"(0(, [03]){20,})(?=(.*\1){3})",g:=str([*zip(*g[::-1])]))or"_")[0],"() 0(?=((,[^,]*){31}|, )[1-9]),"][k>9],"*([3]*len([\\1])or[-.0]),",g)),k-1)
import re;p=lambda g,k=15:-k*g or p(eval(re.sub(*[["\((%s|(0, )+3, 3, 3),?"%(re.search(r"(0(, [03]){20,})(?=(.*\1){3})",g:=str([*zip(*g[::-1])]))or"_")[0],r"(*[3]*len([\1]),"],["0(?=((,[^,]*){31}|, )[1-9])","-.0"]][k>9],g)),k-1)
import re;p=lambda g,k=15:-k*g or p(eval(re.sub(*[["\((%s|(0, )+3, 3, 3),?"%(re.search(r"([ ,03]{61,})(?=(.*\1){3})",g:=str([*zip(*g[::-1])]))or"_")[0],r"(*[3]*len([\1]),"],["(?=0((,[^,]*){31}|, )[1-9])","-."]][k>9],g)),k-1)

### joking (227 (290 unzipped) bytes)
def p(g):
 for y in range(32):g=[[g[y][~x]+13*any({*r[-2%(30-x):31-x]}-{0,3}for r in g[y-1:y+2])for y in range(30)]for x in range(30)];g=[[r[x]%13|3*(len(w:=[r[x]for r in g if{*r[:10]}<={0,3}])>3!={*r[:10]}<={0,3}>={*w}or 3in r[x:]!={*r[:10]}<={0,3})for x in range(30)]for r in g]
 return g

##
def p(g):
 for y in range(#[*range(32,40,4)]##):g=[[g[y][~x]+#[*range(10,50)]##*any({*r[-2%(30-x):31-x]}-{0,3}for r in g[y-1:y+2])for y in range(30)]for x in range(30)];g=[[r[x]%#[prev_vals[-1]]##|3*(len(w:=[r[x]for r in g if{*r[:10]}<={0,3}])>3!={*r[:10]}<={0,3}>={*w}or 3in r[x:]!={*r[:10]}<={0,3})for x in range(30)]for r in g]
 return g

### ovs (233 (267 unzipped) bytes)
def p(g):
 for S in[{0,3}]*8:g=[[g[y][~x]+10*any({*r[-2%(30-x):31-x]}-S for r in g[y+y%~y:y+2])for y in range(30)]for x in range(30)];g=[[r[x]%10|3*({*r[:10]}<=S)*(len(w:=[r[x]for r in g if{*r[:10]}<=S])>3!=S>={*w}or 3in r[x:])for x in range(30)]for r in g]
 return g

### combined (273 (313 unzipped) bytes)
def p(g):
 R=range(30);g=[[g[y][x]+10*any(sum(s[x-(x>0):x+2])for s in g[y-(y>0):y+2])for x in R]for y in R]
 for _ in'_'*8:
  g=*map(list,zip(*g[::-1])),;w=[r for r in g if{*r[:10]}<={0,3}]
  for x in R:
   for r in w:w*=all(r[x]%3<1for r in w);r[x]|=3*(len(w)>3or 3in r[x+1:])
 return[[c%10for c in r]for r in g]
