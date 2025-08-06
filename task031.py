p=lambda m,i=2:i and p([[*l]for l in zip(*m)if sum(l)],i-1)or m
###
p=lambda m,i=0:m*(i>1)or p([[*l]for l in zip(*m)if sum(l)],i+1)
p=lambda m,i=0:m*(i>1)or p([*map(list,filter(sum,zip(*m)))],i+1)
p=lambda m,i=0:m*(i>1)or p([*map(list,zip(*filter(sum,m)))],i+1)