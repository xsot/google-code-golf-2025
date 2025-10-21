import re;p=lambda i,k=3:-k*i or[*zip(*eval(re.sub(f"0(?=({(s:='.%s.0'%{3*len(i)})}, 0)*{s}, ., [^0]{s*2}, (.))","\\2",str(p(i,k-1)))))][::-1]

## if we get the group up to \8, we can avoid the escape
import re;p=lambda i,k=3:-k*i or[*zip(*eval(re.sub("0(?=(%s0)*%s., [^0]%s?%s(.))"%(('.%s.0(, )'%{3*len(i)},)*4),"\\6",str(p(i,k-1)))))][::-1]