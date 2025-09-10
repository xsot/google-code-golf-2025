import re
p=lambda i:max([i[("5"in(s:=str(i)))*(k:=len(i[0])*3-2):]]+[p(eval(r))for l in[("5,? ?"*3,"2,"*3),("5(.{%d}...)?"%k*3,r"2\1 2\2 2\3"),("5, 5(.{%d})5, 5"%k,r"8,8\1 8,8")]if(r:=re.sub(*l,s,1))!=s])

##

def p(g,*S):
 w=len(g[0])
 for c in-6&len(S)+4,5:
  for I in S:g[I//w][I%w]=c
  try:f=sum(g,[])*2;i=f.index(5);[{5}-{c}=={f[I]for I in s}!=g==p(g,i,*s)>1for s in[[w+i,1+i,w-~i],[i+1,i+2],[i+w,i+w*2]]]
  except:return g
