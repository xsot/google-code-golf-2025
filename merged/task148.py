# combined (169 vs 143 bytes for gold)
p=lambda i,l=[0],t=0:[[-y%12&6or(max(x[b:])*max(x[:b+1])>-l[0])*8for b,y in enumerate(x)]for x in i if(l:=l[(t:=t+(i[0]!=x[0])+(i[-1]!=(i:=x)[-1]))>4:]+[8in x]*(2in x))]
