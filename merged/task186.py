# joking (61 bytes, gold)
p=lambda m:[(c:=sum(sum(m,z:=[0]*3))*[2]+z)[:3],[0,c[3],0],z]
#i wonder if you can use zip to truncate in these type of tasks

### ovs (tied, 61 bytes)
*z,p=0,lambda m:[(c:=sum(sum(m,z))*[2]+z*4)[:3],z+c[3:5],z*3]

### xsot (66 bytes)
p=lambda m:[[*(c:=sum(sum(m,[])))*[2],0,0][:3],[0,c//4*2,0],[0]*3]
##
p=lambda m:[[*(c:=sum(sum(m,[])))*[2],0,0][:3],[0,c//4*2,0],[0]*3]
p=lambda m,a=[0]*3:[((c:=sum(sum(m,[])))*[2]+a)[:3],[0,c//4*2,0],a]

### combined (66 bytes)
p=lambda i:[[2,2%-~(k:=sum(sum(i,[]))),k//3*2],[0,k//4*2,0],[0]*3]
