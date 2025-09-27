p=lambda i,k=4,*w:k and p([*map(p,i,[k>1]*9,i[:1]+i,i[1:]+i,*w)],k-1)or i or(sum(w)>7)*7

##

p=lambda i,v=11:-v*i or[[q+(v&(v:=v*2+q%3)>>9&1>>q)*7for q in r]for r in zip(*p(i,v-1)[::-1])]
