p=lambda i,n=1,*w:any(w==(w:=[*map(len,s:=str(i).split(str(n)))][1:-1])for n in{max(i[:3])[0]:0,n:0})*eval('5'.join(s))or p(i,n+1)
