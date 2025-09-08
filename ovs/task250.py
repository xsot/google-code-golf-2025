import re
p=lambda i:[i:=eval(re.sub("5(((.{34}0)+)(.{32})|([0, ]+)), 2",r"0\2\5+5\4,2",str([*zip(*i[::-1])])))for _ in i][7]

##

T=10
def p(g):
 *E,=enumerate(f:=sum(g,[]))
 for J,v in E:
  if v==5:g[J//T][J%T]=0;_,I=min({(abs(a//T-J//T)+abs(a%T-J%T),a)for d in b'*+,! "456'for i,v in E if v==2>f[a:=i+d-43]});g[I//T][I%T]=5
 return g
