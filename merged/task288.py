# ovs (91 vs 88 bytes for gold)
def p(i,n=0):
 l=len(i)//2;*w,S,L=i
 for x in w[l-0**S[-l]:]:x[n]=x[~n]=L[l];n+=1
 return i

### joking (92 bytes)
def p(i,n=0):
 l=len(i)//2
 for x in i[l-0**i[-2][-l]:-2]:x[n]=x[~n]=i[-1][l];n+=1
 return i

### combined (112 bytes)
p=lambda i,e=enumerate:[[y or i[-1][t:=len(i)//2]*(a+abs(b-t)==t*2-0**i[-2][-t])for b,y in e(x)]for a,x in e(i)]
