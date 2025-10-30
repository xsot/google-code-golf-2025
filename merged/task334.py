# joking (69 bytes, gold)
p=lambda i:[[(y>>max(max(i)))%2*5for y in[x,x|6,x|8]]for x in[4,2,8]]

## experiments with recursion
p=lambda i,r=[4,2,8],w=0:i*0!=0and[p(max(i),[0,6,8],w|n)for n in r]or(w>>i&1)*5
p=lambda i,r=[4,2,8,0,6,8],w=0:r and[p(max(i),r[3:],w|n)for n in r[:3]]or(w>>i&1)*5
p=lambda i,r=[4,2],w=0:i*0!=0and[p(max(i),[0,6],w|n)for n in r+[8]]or(w>>i&1)*5
p=lambda i,w=0:i*0!=0and[p(max(i),w|n)for n in[4<<w&7,6//~w&6,8]]or(w>>i&1)*5
p=lambda i,w=0:i*0!=0and[*map(p,[max(i)]*3,[w or 4,w|2|-w%6,w|8])]or(w>>i&1)*5
p=lambda i,w=0:i*0!=0and[p(max(i),n)for n in[w or 4,w|2|-w%6,w|8]]or(w>>i&1)*5
p=lambda i,r=[4,2,8,0,6,8],w=0:r and[p(max(i),r[3:],w|n)for n in r[:3]]or(w>>i&1)*5

### xsot (tied, 69 bytes)
p=lambda i:[[((x|y)>>max(max(i))&1)*5for y in[0,6,8]]for x in[4,2,8]]

##
p=lambda m:[[x:=[0,5,0],y:=[5]*3,x],[y,x,x],[z:=[0,0,5],z,y]][max(max(m))-1]
p=lambda m:[[[0,5,0],[5,5,5],[0,5,0]],[[5,5,5],[0,5,0],[0,5,0]],[[0,0,5],[0,0,5],[5,5,5]]][max(max(m))-1]

### combined (75 bytes)
p=lambda i:[[((x|y)>>sum({*sum(i,[])})&1)*5for y in[0,6,8]]for x in[4,2,8]]
