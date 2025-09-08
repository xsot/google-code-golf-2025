import re;p=lambda i,k=27:-k*[x[1:10]for x in i[1:10]]or p(eval(re.sub(f"(([13-9]).*)2, 0(.{ {len(i)*3}}.)0, 0",r"\1\2,\2\3\2,2",str([*zip(*i[::-1],[0]*11)]))),k-1)


##
import re;p=lambda i,k=27:-k*i or p([x[:9]for x in eval(re.sub(f"(([13-9]).*)2, 0(.{ {len(i)*3}}.)0, 0",r"\1\2,\2\3\2,2",str([*zip(*i,[0]*9),[0]*10])))[8::-1]],k-1)
p=lambda i,k=27,f=[0]*9:-k*i or[[(u==2>1>s+t)*2or(s*t*y>1or 2in[s,t]*u)*max({*sum(i,[])}-{2})or y for y,s,t,u in zip(x,[0]+x,f,[0]+f)]+[f:=x]*0for*x,in zip(*p(i,k-1))][::-1]
