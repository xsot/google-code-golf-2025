# ovs (111 vs 108 bytes for gold)
p=lambda i,k=11,t=1:-k*i or p([(e:=1)*[e:=y%2*[y|(t:=t*16)|e,-y%5][k<1]for y in i]for i[::-1]in zip(*i)],k-1,0)

### joking (113 bytes)
p=lambda i,k=11,t=1:-k*i or[(e:=1)*[e:=y%2*[y|(t:=t*16),-y%5,e|y][k//-10]for y in i]for i[::-1]in zip(*p(i,k-1))]

##
p=lambda i,k=39,t=1:-k*i or[(e:=0)or[e:=[y%2*(t:=t*16),-y%5,y%~y&e|y][k//-38]for y in x]for*x,in zip(*p(i,k-1)[::-1])]
p=lambda i,k=39,z=4:-k*i or p([(e:=1)*[e:=y and[e|(y<6)*(z:=z*4)|y,-y%3+1][k<1]for y in x]for*x,in zip(*i[::-1])],k-1)
p=lambda i,k=11,t=1:-k*i or p([(e:=1)*[e:=y%2*[-y%5,y|[e,t:=t*16][y<6]][k>0]for y in i]for i[::-1]in zip(*i)],k-1)
p=lambda i,k=11,t=1:-k*i or[(e:=1)*[e:=y%2*[-y%5,y|[e,t:=t*16][k<1]][k<11]for y in i]for i[::-1]in zip(*p(i,k-1))]
p=lambda i,k=11,t=1:-k*i or[[e:=y%2and[y|(t:=t*16),-y%5,e|y][k//-10]for y in[0]+i][:0:-1]for*i,in zip(*p(i,k-1))]

### att (117 bytes)
p=lambda i,k=39,t=1:-k*i or[(e:=0)or[e:=[y%2*(t:=t*16),-y%5,y%~y&e|y][k//-38]for y in i]for i[::-1]in zip(*p(i,k-1))]

### combined (134 bytes)
p=lambda i,k=39,t=0:-k*i or[[[y and y|e,-len(y)%5][k>38]if k else{*[t:=t+1]*y}for y,e in zip(x,x[:1]+x)]for x in zip(*p(i,k-1)[::-1])]
