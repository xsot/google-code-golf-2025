p=eval(f"lambda i:[i:=[[i[~b][a]|(i[-b][a-1]==2)*4+(i[-b][a]==1)*7{'for %s in range(9)]'*3%(*'ba_',)}[3]")

## experiments with using true/false
p=lambda i:[i:=[[s!=2and~-len(str(s))|y|(s==1)*7for y,s in zip(x,[0,*x])]for x in zip(*i[::-1])]for _ in i][7]
p=lambda i:[i:=[[y==1or s!=2and y|6-len(str(s))^5for y,s in zip(x,[0,*x])]for x in zip(*i[::-1])]for _ in i][7]