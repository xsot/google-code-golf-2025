# combined (75 vs 2500 bytes for gold)
p=lambda i:[(h:=[8]*sum({*x}=={0,5}for x in i)+[0]*5)[1:4],h[6:3:-1],[0]*3]

### xsot (77 bytes)
p=lambda m:[[*[8]*(c:=str(m).count("0, 5, 0")//2),0,0][:3],[0,0,4+c&8],[0]*3]
##
p=lambda m:[[*[8]*(c:=str(m).count("0, 5, 0")//2),0,0][:3],[0,0,c//4*8],[0]*3]
