import re;p=lambda i,w=2:s!=(r:=re.sub((w%2*"5, "+"5(.%s)??")%{w*3%-7%len(i[0]*3)+2}*(3-w%2),r" 82,\81\ 12 \82, 82"[w::2],s,1))and p(eval(r))or w and p(i,w-1)if"5"in(s:=str(i))else i

##
import re;p=lambda i:max([i[("5"in(s:=str(i)))*(k:=len(i[0])*3-2):]]+[p(eval(r))for l in[("5,? ?"*3,"2,"*3),("5(.%s)?"%{k+3}*3,r"2\1 2\2 2\3"),("5, 5(.%s)5, 5"%{k},r"8,8\1 8,8")]if(r:=re.sub(*l,s,1))!=s])
import re;p=lambda i,w=2:s!=(r:=re.sub(w%2*("5, 5(.%s)5, 5"%{k:=len(i[0])*3-2})or"5(.%s)??"%{2-w//2*~k}*3,r" 82,\81\ 12 \82, 82"[w::2],s,1))and p(eval(r))or w and p(i,w-1)if"5"in(s:=str(i))else i
import re;p=lambda i,w=2:s!=(r:=re.sub((w%2*"5, "+"5(..%s)??")%{(k:=len(i[0])*3,k-3,1)[w]}*(3-w%2),r" 82,\81\ 12 \82, 82"[w::2],s,1))and p(eval(r))or w and p(i,w-1)if"5"in(s:=str(i))else i