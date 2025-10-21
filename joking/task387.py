p=lambda i,k=6,e=enumerate,S=sum:~k*i or p([[y or([(S(x[b:])*S(x[:b])%5>S(r:=S([(),*zip(*i[b+b%~b:b+2])][a:a+3],()))<x[b-2]+x[b+2])*5,*{*S(i,[])}-{*r,5}]*3)[3>>k]for b,y in e(x)]for a,x in e(zip(*i))],k-2)

##
p=lambda i,k=7,e=enumerate,S=sum:-k*i or p([[y or([(S(x[b:])*S(x[:b])%5>S(r:=S([*zip(*i[b+b%~b:b+2])][a+a%~a:a+2],()))<x[b-2]+x[b+2])*5,*{*S(i,[])}-{*r,5}]*3)[7>>k]for b,y in e(x)]for a,x in e(zip(*i))],k-2)