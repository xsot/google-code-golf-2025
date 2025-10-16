p=lambda i,k=7,*w:k and p([*map(p,i,[k>1]*99,[i*2]+i,i[1:]+[i*2],*w)],k-1)or((c:=w.count)(2)+c(4)>=2!=i)*4or i


##
import re;p=lambda i,k=23:-k*i or p(eval(re.sub(f"(?<=[24], )[^2](?=(.{ {len(i)*3}}|.) [24])","4",str([*zip(*i[::-1])]))),k-1)
p=lambda i,k=7,*w:k and p([*map(p,i,[k>1]*99,i[:1]+i,i[1:]+i[-1:],*w)],k-1)or((c:=w.count)(2)+c(4)>=2!=i)*4or i