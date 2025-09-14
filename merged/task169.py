# ovs (121 vs 129 bytes for gold)
p=lambda i,k=39,t=1:-k*i or[[[y%2*(t:=t*16),-y%5,y and y|e][k//-38]for y,e in zip(x,[0]+x)]for*x,in zip(*p(i,k-1)[::-1])]

### combined (134 bytes)
p=lambda i,k=39,t=0:-k*i or[[[y and y|e,-len(y)%5][k>38]if k else{*[t:=t+1]*y}for y,e in zip(x,x[:1]+x)]for x in zip(*p(i,k-1)[::-1])]
