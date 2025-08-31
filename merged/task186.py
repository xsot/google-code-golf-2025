# xsot (66 vs 60 bytes for gold)
p=lambda m:[[*(c:=sum(sum(m,[])))*[2],0,0][:3],[0,c//4*2,0],[0]*3]
##
p=lambda m:[[*(c:=sum(sum(m,[])))*[2],0,0][:3],[0,c//4*2,0],[0]*3]
p=lambda m,a=[0]*3:[((c:=sum(sum(m,[])))*[2]+a)[:3],[0,c//4*2,0],a]

### combined (tied, 66 bytes)
p=lambda i:[[2,2%-~(k:=sum(sum(i,[]))),k//3*2],[0,k//4*2,0],[0]*3]
