exec("p=lambda i,n=12:[[i[a][b]or 2*any([n,*[2]*(n-2),n]==[sum(i[(a-k+s)%12][b-j:][:n])/5"+"for %s in range(n)%s"*6%(*'s]n j k)b]a]',))

##
p=lambda i,r=range(12):[[i[a][b]or 2*any([[sum(s[b-j:][:n])/5for s in i[a-k:][:n]]==[n,*[2]*(n-2),n]for n in r for j in r[:n]for k in r[:n]])for b in r]for a in r]
import re;p=lambda i,k=20:-k*i or p(eval(re.sub(f'({(h:=(5,)*-~(n:=k%5))}.{(s:={34-n*3})}(?={(r:=f"5, [^5]{ {n*3}}5.{s}")*n}{h})({r})*5)(, 0)+',"\\1"+",2"*n,str(i))),k-1)
p=lambda i,k=7,r=re.sub,S=str:-k*i or p(eval(r((h:=S((5,)*-~(n:=k%5)))+((s:=f"(.{ {34-n*3}})")+S((5,*[0]*n,5)))*n+s+h,lambda m,s=1:"".join(r(S(s:=1-s),"2",z)for z in m.groups()),S(i))),k-1)
p=lambda i,k=20,r=re.sub,S=str:-k*i or p(eval(r("("+(h:=S((5,)*-~(n:=k%5)))+"(?="+(r:=(s:=f".{ {34-n*3}}")+(y:="5, "+"[02], "*n+"5"))*n+s+h+f")({r})*{s})5"+", 0"*n,f"\\1*{[5]+[2]*n}",S(i))),k-1)
p=lambda i,k=20,r=re.sub:-k*i or p(eval(r(f'({(h:=(5,)*-~(n:=k%5))}(?={(r:=(s:=f".{ {34-n*3}}")+"5, "+"[02], "*n+"5")*n+s}{h})({r})*{s})5'+", 0"*n,f"\\1*{[5]+[2]*n}",str(i))),k-1)
exec("p=lambda i,n=12:[[i[a][b]or 2*any([sum(s[b-j:][:n])/5for s in i[a-k:][:n]]==[n,*[2]*(n-2),n]"+"for %s in range(n)%s"*5%(*'n j k)b]a]',))