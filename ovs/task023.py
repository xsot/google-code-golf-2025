import re;p=lambda i,w=2:s!=(r:=re.sub(("5(, )?"*3,"5, 5(.%s)5, 5"%{k:=len(i[0])*3-2},"5(.%s)?"%{k+3}*3)[w],w%2*r"8,8\1 8,8"or r"2\1 2\2 2\3",s,1))and p(eval(r))or w and p(i,w-1)if"5"in(s:=str(i))else i

##

def p(g,*S):
 w=len(g[0])
 for c in-6&len(S)+4,5:
  for I in S:g[I//w][I%w]=c
  try:f=sum(g,[])*2;i=f.index(5);[{5}-{c}=={f[I]for I in s}!=g==p(g,i,*s)>1for s in[[w+i,1+i,w-~i],[i+1,i+2],[i+w,i+w*2]]]
  except:return g
