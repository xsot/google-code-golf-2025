# joking (71 bytes, gold)
p=lambda i:[(h:=[8for x in i if sum(x)==10]+[0]*5)[:3],h[5:2:-1],[0]*3]

### combined (75 bytes)
p=lambda i:[(h:=[8]*sum({*x}=={0,5}for x in i)+[0]*5)[1:4],h[6:3:-1],[0]*3]

### xsot (77 bytes)
p=lambda m:[[*[8]*(c:=str(m).count("0, 5, 0")//2),0,0][:3],[0,0,4+c&8],[0]*3]
##
p=lambda m:[[*[8]*(c:=str(m).count("0, 5, 0")//2),0,0][:3],[0,0,c//4*8],[0]*3]
