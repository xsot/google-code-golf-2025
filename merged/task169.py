# joking+mwi (134 vs 131 bytes for gold)
p=lambda i,k=39,t=0:-k*i or[[[y and y|e,-len(y)%5][k>38]if k else{*[t:=t+1]*y}for y,e in zip(x,x[:1]+x)]for x in zip(*p(i,k-1)[::-1])]
