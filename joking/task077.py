p=lambda i,k=5,*w,r=[[0]*25]:-k*i or i*0!=0and p([*map(p,i,*r,r+i,i[1:]+r,*w)],k-1)or((c:=w.count)(2)+c(4)>=2!=i)*4or i


##
import re;p=lambda i,k=23:-k*i or p(eval(re.sub(f"(?<=[24], )[^2](?=(.{ {len(i)*3}}|.) [24])","4",str([*zip(*i[::-1])]))),k-1)