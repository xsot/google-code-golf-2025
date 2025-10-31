# joking (94 vs 91 bytes for gold)
p=lambda i,k=0,*s:[s+(s:=())for x in zip(*k or p(i,i))if-~-any(x)*(s:=(*map(max,s+x,x),))]+[s]
# you might be able to do this recursively to iterate across each item, but idk how you would also do the zip with that

##
p=lambda i,k=0,s=[0]*99:[s+0*(s:=x)for*x,in zip(*k or p(i,i))if-~-any(x)*(s:=[*map(max,s,x)])]+[s]
r=[0]*99;p=lambda i,k=0,s=r:[s+0*(s:=x)for*x,in zip(*k or p(i,i))if r+(s:=[*map(max,s,x)])>x]+[s]
r=[0]*99;p=lambda i,k=0,s=r:[s+0*(s:=x)for*x,in[*zip(*k or p(i,i)),r]if r+(s:=[*map(max,s,x)])>x]
p=lambda i,k=0,s=[]:[s+0*(s:=x)for*x,in zip(*k or p(i,i))if-~-any(x)*(s:=[*map(max,s+x,x)])]+[s]
p=lambda i,k=0,*s:[s+0*(s:=x)for x in zip(*k or p(i,i))if-~-any(x)*(s:=(*map(max,s+x,x),))]+[s]
p=lambda i,*k,s=[]:[s+(s:=[])for*x,in zip(*k or p(i,*i))if-~-any(x)*(s:=[*map(max,s+x,x)])]+[s]

### combined (101 bytes)
p=lambda i,k=0,s=[0]*99:[s+0*(s:=[*x])for x in zip(*k or p(i,i))if-~-any(x)*(s:=[*map(max,s,x)])]+[s]
