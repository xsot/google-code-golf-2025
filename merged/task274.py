# joking (71 vs 65 bytes for gold)
p=lambda i:[(h:=[8for x in i if sum(x)==10]+[0]*5)[:3],h[5:2:-1],[0]*3]

##
p=lambda i:[(h:=[8]*[*map(sum,i)].count(10)+[0]*5)[:3],h[5:2:-1],[0]*3]
*r,p=0,lambda i:[(h:=[8]*[*map(sum,i)].count(10)+r*6)[:3],h[5:2:-1],r*3]
p=lambda i,r=[0]*3:[(h:=[8]*[*map(sum,i)].count(10)+r*2)[:3],h[5:2:-1],r]
p=lambda i:[(h:=str(i).count("0, 5, 0")//2*[8]+[0]*5)[:3],h[5:2:-1],[0]*3]
p=lambda i:[(h:=str(i).count("0, 5, 0")*[8]+[0]*9)[:6:2],h[10:4:-2],[0]*3]

### combined (75 bytes)
p=lambda i:[(h:=[8]*sum({*x}=={0,5}for x in i)+[0]*5)[1:4],h[6:3:-1],[0]*3]

### xsot (77 bytes)
p=lambda m:[[*[8]*(c:=str(m).count("0, 5, 0")//2),0,0][:3],[0,0,4+c&8],[0]*3]
##
p=lambda m:[[*[8]*(c:=str(m).count("0, 5, 0")//2),0,0][:3],[0,0,c//4*8],[0]*3]
