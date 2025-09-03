# combined (188 vs 175 bytes for gold)
p=lambda i,k=3,e=enumerate:-k*i or[[y|((a-~b>(t:=len(x)-1))*i[0][-1]+b*2//t*i[-1][-1]+a*2//t*i[0][0]<~max(a,b)%2)*i[-1][0]for b,y in e(x)]for a,x in e(zip(*p([*zip(*i[::-1])],k-1)))][::-1]
