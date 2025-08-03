p=lambda m:[(l:=m[(170>>r)%3])[::-1]+l for r in range(9)]
# p=lambda m:[[m[(170>>r)%3][c%3<1]for c in range(4)]for r in range(9)]
# p=lambda m:[[m[[2-r%3,r%3][r//3%2]][c%3<1]for c in range(4)]for r in range(9)]