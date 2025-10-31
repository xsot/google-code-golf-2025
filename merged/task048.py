# att (118 vs 92 bytes for gold)
p=lambda m,i=99,s="":-i*[[8-8*("2"in'%s'%m)]]or p([*zip(*eval(str(m).replace("282"[i%3]+s,"1"+s,2)))][::-1],i-1,", 1")

### xsot (120 bytes)
# change the first red to blue, then flood fill from blue and test if any red is left
p=lambda m,i=99,s="":-i*[[8-8*("2"in str(m))]]or p([*zip(*eval(str(m).replace("28"[i%3%2]+s,"1"+s,1)))][::-1],i-1,", 1")

##
# alt, replace 2,2 -> 1,1
p=lambda m,i=99:-i*[[8-8*("2"in str(m))]]or p([*zip(*eval(str(m).replace("28"[i%3%2]+", "+"21"[i<99],"1,1",1)))][::-1],i-1)

p=lambda m,i=99:-i*[[8-8*("2"in str(m))]]or p([*zip(*eval(str(m).replace([["2, 2","2, 1"][i<99],"8, 1"][i%3%2],"1,1",1)))][::-1],i-1)
p=lambda m,i=99:-i*[[8-8*("2"in str(m))]]or p([*zip(*eval(str(m).replace([["2","2, 1"][i<99],"8, 1"][i%3%2],["1","1,1"][i<99],1)))][::-1],i-1)

### combined (120 bytes)
p=lambda m,i=99,s="":-i*[[8-8*("2"in str(m))]]or p([*zip(*eval(str(m).replace("28"[i%3%2]+s,"1"+s,1)))][::-1],i-1,", 1")

### mwi (136 bytes)
# an interesting detail about the generator: all cases are solvable whether you include diagonal adjacencies or ignore them
# https://github.com/google/ARC-GEN/blob/c698c57de8ace891e82b593488136cfb339fb5a5/tasks/training/task048.py#L69
p=lambda i,r=1,k=40:-k*[[8-8*("2"in str(i))]]or p([[(y>=1==s)or y-r+(r:=y!=2<r*3)for s,y in zip([0,*x],x)]for x in zip(*i[::-1])],0,k-1)
