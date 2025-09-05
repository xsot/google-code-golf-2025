# combined (82 vs 2500 bytes for gold)
p=lambda i,E=enumerate:[[5+(y<5)*i[a&12|1][b&12|1]for b,y in E(x)]for a,x in E(i)]

### att (85 bytes)
p=lambda a:[*map(f:=lambda*b:sum(([5]+3*[e%5+5]for e in b[1::4]),[])[1:],*map(f,*a))]
