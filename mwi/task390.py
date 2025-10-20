import re
p=lambda g:[g:=eval(re.sub("([^2(]{9}2[^2]{9})",r"*[\1][::-1]","%s"%[*zip(*g)]))for _ in g][1]

##
p=lambda g:[g:=[*zip(*[[*[g[k-~k]for k in(1,2,-3,-4)if g[k].count(2)>4],r][0]for r in g if(g:=g[1:]+[r])])]for _ in g][1]
p=lambda g:[g:=[*zip(*"2, "*3in"%s"%g and g[:(i:=g.index(max(g)))-3]+g[i+3:i+1:-1]+g[i-1:i+2]+g[:2]+g[i+4:]or g)][::-1]for _ in g][3]