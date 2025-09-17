# xsot (69 vs 66 bytes for gold)
p=lambda i:[[((x|y)>>max(max(i))&1)*5for y in[0,6,8]]for x in[4,2,8]]

##
p=lambda m:[[x:=[0,5,0],y:=[5]*3,x],[y,x,x],[z:=[0,0,5],z,y]][max(max(m))-1]
p=lambda m:[[[0,5,0],[5,5,5],[0,5,0]],[[5,5,5],[0,5,0],[0,5,0]],[[0,0,5],[0,0,5],[5,5,5]]][max(max(m))-1]

### combined (75 bytes)
p=lambda i:[[((x|y)>>sum({*sum(i,[])})&1)*5for y in[0,6,8]]for x in[4,2,8]]
