import re;p=lambda i:exec(r"i[::-1]=zip(*eval(re.sub('0(?=(%s 0)*%s ., [^0]%s?%s (.))'%(('.%s.0,'%{3*len(i)},)*4),'\\2',str(i))));"*4)or i

##

def p(g,k=-3):u=range(len(g)-2);[exec("q-=1;P-=1;g[q][P]=g[y+2][x+2];"*min(P:=x,q:=y)*(g[y+1][x+1]<g[y+1][x]&g[y][x+1]))for y in u for x in u];return g*k or p([*map(list,zip(*g[::-1]))],k+1)
