
p=lambda i,k=7,s=0:-k*i or[[k<7and(-((s:=(y>0)*min(s-1,-1)or~-max(-s,s,1))>1)or y)or(z:=[*{}.fromkeys(sum(i,[]))])[y and~(y!=z[1])]for y in x]for x in zip(*p(i,k-1)[::-1])]

##alt
p=lambda i,k=7,s=0:-k*i or p([[k and(-((s:=(y>0)*min(s-1,-1)or~-max(-s,s,1))>1)or y)or(z:=[*{}.fromkeys(sum(i,[]))])[y and~(y!=z[2])]for y in x]for x in zip(*i[::-1])],k-1)