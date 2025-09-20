import re;p=lambda i,k=7:-k*i or[*zip(*eval(re.sub("(?=(.{32})*(., |.{29})?2, [^0].{25}([13-9]))\d","\\3",str(p(i,k-1)))))][::-1]

##
import re;p=lambda i,k=27:-k*[x[1:10]for x in i[1:10]]or p(eval(re.sub(f"(([13-9]).*)2, 0(.{ {len(i)*3}}.)0, 0",r"\1\2,\2\3\2,2",str([*zip(*i[::-1],[0]*11)]))),k-1)
import re;p=lambda i,k=27:-k*i or p([x[:9]for x in eval(re.sub(f"(([13-9]).*)2, 0(.{ {len(i)*3}}.)0, 0",r"\1\2,\2\3\2,2",str([*zip(*i,[0]*9),[0]*10])))[8::-1]],k-1)
p=lambda i,k=27,f=[0]*9:-k*i or[[(u==2>1>s+t)*2or(s*t*y>1or 2in[s,t]*u)*max({*sum(i,[])}-{2})or y for y,s,t,u in zip(x,[0]+x,f,[0]+f)]+[f:=x]*0for*x,in zip(*p(i,k-1))][::-1]
p=lambda i,k=20,m=0,*w,r=[[0]*10]*10:k and p([*map(p,i,[k>1]*10,[m or max({*sum(i,[])}-{2})]*10,r[:1]+i,i[1:]+r,*w)],k-1)or[m,i][-2!=i!=2]or(w.count(-2)&2)-(2in w)*2
