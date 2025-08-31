# xsot (120 vs 95 bytes for gold)
# change the first red to blue, then flood fill from blue and test if any red is left
p=lambda m,i=99,s="":-i*[[8-8*("2"in str(m))]]or p([*zip(*eval(str(m).replace("28"[i%3%2]+s,"1"+s,1)))][::-1],i-1,", 1")

##
# alt, replace 2,2 -> 1,1
p=lambda m,i=99:-i*[[8-8*("2"in str(m))]]or p([*zip(*eval(str(m).replace("28"[i%3%2]+", "+"21"[i<99],"1,1",1)))][::-1],i-1)

p=lambda m,i=99:-i*[[8-8*("2"in str(m))]]or p([*zip(*eval(str(m).replace([["2, 2","2, 1"][i<99],"8, 1"][i%3%2],"1,1",1)))][::-1],i-1)
p=lambda m,i=99:-i*[[8-8*("2"in str(m))]]or p([*zip(*eval(str(m).replace([["2","2, 1"][i<99],"8, 1"][i%3%2],["1","1,1"][i<99],1)))][::-1],i-1)
