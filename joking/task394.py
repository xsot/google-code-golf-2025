p=lambda i:[[max(x[b%(n:=2+len(i)//7)::n])for b,y in enumerate(x)if y<1]for x in i if 0in x]

## recursion experiment
p=lambda i,v=0,n=0:i*0!=0and[p(y,v,122%len(i))for y,v in zip(i,i[n:n*2]+i)if'0'in'%s'%y]or v