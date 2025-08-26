p=lambda m:[r[::-1]+r for r in(m[::-1]+m)*2][:9]

##
p=lambda m:[r[::-1]+r for r in m[::-1]+m+m[::-1]]
p=lambda m:(a:=[r[::-1]+r for r in m[::-1]])+a[::-1]+a
p=lambda m:[(l:=m[(170>>r)%3])[::-1]+l for r in range(9)]
p=lambda m:[[m[(170>>r)%3][c%3<1]for c in range(4)]for r in range(9)]
p=lambda m:[[m[[2-r%3,r%3][r//3%2]][c%3<1]for c in range(4)]for r in range(9)]