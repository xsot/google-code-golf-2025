# combined (126 vs 100 bytes for gold)
p=lambda m,k=3,R=range(-14,1):-k*m or p([*zip(*[m[(len([l:=i-j for j in R if 2in m[-j]])==4>abs(l)>1)*2*l-i]for i in R])],k-1)

### xsot (136 bytes)
# for each row close enough (but not too close) to the first red row, replace it with the row reflected around the red
# 4==len(d) makes sure we only apply the transform when reds are horizontal
p=lambda m,k=3,R=range(15):-k*m or p([*zip(*[m[(1<abs((d:=[j-i for j in R if 2in m[j]])[0])<4==len(d))*2*d[0]+i]for i in R][::-1])],k-1)
