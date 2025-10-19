p=lambda i:[[(y>>max(max(i)))%2*5for y in[x,x|6,x|8]]for x in[4,2,8]]

## experiments with recursion
p=lambda i,r=[4,2,8],w=0:i*0!=0and[p(max(i),[0,6,8],w|n)for n in r]or(w>>i&1)*5
p=lambda i,r=[4,2,8,0,6,8],w=0:r and[p(max(i),r[3:],w|n)for n in r[:3]]or(w>>i&1)*5
p=lambda i,r=[4,2],w=0:i*0!=0and[p(max(i),[0,6],w|n)for n in r+[8]]or(w>>i&1)*5
p=lambda i,w=0:i*0!=0and[p(max(i),w|n)for n in[4<<w&7,6//~w&6,8]]or(w>>i&1)*5
p=lambda i,w=0:i*0!=0and[*map(p,[max(i)]*3,[w or 4,w|2|-w%6,w|8])]or(w>>i&1)*5
p=lambda i,w=0:i*0!=0and[p(max(i),n)for n in[w or 4,w|2|-w%6,w|8]]or(w>>i&1)*5
p=lambda i,r=[4,2,8,0,6,8],w=0:r and[p(max(i),r[3:],w|n)for n in r[:3]]or(w>>i&1)*5