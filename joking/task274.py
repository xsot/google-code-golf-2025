p=lambda i:[(h:=[8for x in i if sum(x)==10]+[0]*5)[:3],h[5:2:-1],[0]*3]

##
p=lambda i:[(h:=[8]*[*map(sum,i)].count(10)+[0]*5)[:3],h[5:2:-1],[0]*3]
*r,p=0,lambda i:[(h:=[8]*[*map(sum,i)].count(10)+r*6)[:3],h[5:2:-1],r*3]
p=lambda i,r=[0]*3:[(h:=[8]*[*map(sum,i)].count(10)+r*2)[:3],h[5:2:-1],r]
p=lambda i:[(h:=str(i).count("0, 5, 0")//2*[8]+[0]*5)[:3],h[5:2:-1],[0]*3]
p=lambda i:[(h:=str(i).count("0, 5, 0")*[8]+[0]*9)[:6:2],h[10:4:-2],[0]*3]