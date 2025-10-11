# feels golfable
p=lambda i,k=3,s=0,S=sum:-k*i or p([[y|(s==5in{*(h:=[*map(S,i)])[b+1:]}&{*h[:b]})*S({*S(i,[-5])})for b,y in enumerate(x)]+0*[s:=s*2+S(x)]for x in zip(*i)][::-1],k-1)

## no enumerate
p=lambda i,k=3,s=0:-k*i or p([[s:=s*2+max(x),b:=0]and[y|(5in{*(h:=[*map(max,i)])[:b]}&{*h[(b:=b+1):]}!=5<s<20)*sum({*sum(i,[])},-5)for y in x]for x in zip(*i)][::-1],k-1)