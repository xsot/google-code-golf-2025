# replacing [1:4] with [1:] saves a byte at the cost of a lot of speed.
# for this version, that removal doesn't save after compression so i left in the 4
def p(g):R=max([{(i,j)for i in range(21)[x:x+3]for j in range(21)[y:y+3]if g[i][j]}for x in range(21)for y in range(21)],key=len);return[[max((c==(y-k*d,x-k*D))*g[i+d][j+D]for i,j in R for d in[-4,0,4]for D in[-4,0,4]for k in range(21)[1:4]for c in R)for x in range(21)]for y in range(21)]

##

p=lambda g:(R:=max([{(i,j)for i in range(21)[I:I+3]for j in range(21)[J:J+3]if g[i][j]}for I in range(21)for J in range(21)],key=len),[[max((c==(y-k*d,x-k*D))*g[i+d][j+D]for i,j in R for d in(-4,0,4)for D in(-4,0,4)for k in range(21)[1:]for c in R)for x in range(21)]for y in range(21)])[1]