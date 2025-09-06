p=lambda i,n=1,w=0:(any(w==(w:=[*map(len,bytes(sum(i,[])).split(b'%c'%n))][1:-1])for n in{n,max(i[:3])[0]}))*eval(str(i).replace(*f"{n}5"))or p(i,n+1)
