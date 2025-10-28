# joking (126 bytes, gold)
import re
p=lambda g,k=-19:k*g or p(eval(re.sub(f"0(?=, 4|.{ {N:=len(g)*3+4}}5, 0.{ {N-6}}0)","4",str([*zip(*g)][::-1]))),k+1)

##
p=lambda g,k=-23:k*g or p(eval(re.sub(f"0, (?=4|..{(N:={len(g)*3-2})}...5, 0.{N}0)","4,",str([*zip(*g)][::-1]))),k+1)
p=lambda g,k=-19:k*g or p(eval(re.sub("0(?=, 4|.%s5, 0.%%s0)"%{N:=len(g)*3+4}%{N-6},"4",str([*zip(*g)][::-1]))),k+1)
import re;p=lambda g:exec('g[:]=zip(*eval(re.sub(f"0(?=, 4|.{ {N:=len(g[0])*3+4}}5, 0.{ {N-6}}0)","4",str(g[::-1]))));'*20)or g
import re;p=lambda g:exec('g[:]=eval(re.sub(f"0(?=, 4|.{ {N:=len(g)*3+4}}5, 0.{ {N-6}}0)","4",str([*zip(*g[::-1])])));'*20)or g

### ovs (127 bytes)
import re
p=lambda g,k=-23:k*g or p(eval(re.sub(f"0, (?=4|5.{(N:={len(g)*3-2})}5, 5, 0.{N}0)","4,",str([*zip(*g)][::-1]))),k+1)

### combined (223 bytes)
p=lambda g,k=59,e=enumerate:-k*g or p([*zip(*[[[c-c%5+0**c*4,max(c,x+y<1,(v:=(*g[y-(y>0)][x-1:x+1],r[x-1]))==(5,0,0),y>1<x<sum(v)>10>4<g[y-1][x-2]+g[y-2][x-1]or[0,*r][x]%5)][k>0]for x,c in e(r)]for y,r in e(g)][::-1])],k-1)
