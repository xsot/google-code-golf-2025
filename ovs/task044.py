p=lambda i:[i:=[[J^c*(1&(w:=w>>1)>>99or J==c)for J in J]for c in{*sum(i,[])}if bin(sum((sum(i,[])[J]==c)<<J+9for J in range(100)))in bin(w:=sum((sum(i,[])[J]<5in{*sum(i,[])[J//10*10:J]}&{*sum(i,[])[J:J//10*10+10]})<<J+100for J in range(50)))for J in i][::-1]for J in i][1]

## 222/461
def p(i):f=sum(i,[]);w=sum(2<<J for J in range(50)if f[J]<5in{*f[J//10*10:J]}&{*f[J:J//10*10+10]});i=[[J^c*(1&(w:=w>>1)or J==c)for J in J]for c in{*f}if bin(sum(512<<J for J in range(100)if f[J]==c))in bin(w<<100)for J in i][::-1];f=sum(i,[]);w=sum(2<<J for J in range(50)if f[J]<5in{*f[J//10*10:J]}&{*f[J:J//10*10+10]});i=[[J^c*(1&(w:=w>>1)or J==c)for J in J]for c in{*f}if bin(sum(512<<J for J in range(100)if f[J]==c))in bin(w<<100)for J in i][::-1];return i

## 226/250
def p(i):
 for J in 0,0:f=sum(i,[]);w=sum((f[J]<5in{*f[J//10*10:J]}&{*f[J:J//10*10+10]})<<J+1for J in range(50));i=[[J^c*(1&(w:=w>>1)or J==c)for J in J]for c in{*f}if bin(sum((f[J]==c)<<J+9for J in range(100)))in bin(w<<99)for J in i][::-1]
 return i

## 230/254
def p(i):
 for I in-1,-1:f=sum(i,[]);w={J for J in range(50)if f[J]<5in{*f[J//10*10:J]}&{*f[J:J//10*10+10]}};i=[[J^c*(w>{I:=I+1}or J==c)for J in J]for c in{*f}if{J-min(w)+f.index(c)for J in w}=={J for J in range(100)if f[J]==c}for J in i][::-1]
 return i
