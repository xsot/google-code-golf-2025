def p(i):f=sum(i,[]);w={J for J in range(50)if f[J]<5in{*f[J//10*10:J]}&{*f[J:J//10*10+10]}};I=-1;i=[[r^c*({I:=I+1}<w|h)for r in r]for c in{*f}if{k-min(w)+f.index(c)for k in w}==(h:={J for J in range(100)if f[J]==c})for r in i][::-1];f=sum(i,[]);w={J for J in range(50)if f[J]<5in{*f[J//10*10:J]}&{*f[J:J//10*10+10]}};I=-1;i=[[r^c*({I:=I+1}<w|h)for r in r]for c in{*f}if{k-min(w)+f.index(c)for k in w}==(h:={J for J in range(100)if f[J]==c})for r in i][::-1];return i

## 237/254

def p(i):
 for I in-1,-1:f=sum(i,[]);w={J for J in range(50)if f[J]<5in{*f[J//10*10:J]}&{*f[J:J//10*10+10]}};i=[[r^c*({I:=I+1}<w|h)for r in r]for c in{*f}if{k-min(w)+f.index(c)for k in w}==(h:={J for J in range(100)if f[J]==c})for r in i][::-1]
 return i
