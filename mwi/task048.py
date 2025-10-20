# an interesting detail about the generator: all cases are solvable whether you include diagonal adjacencies or ignore them
# https://github.com/google/ARC-GEN/blob/c698c57de8ace891e82b593488136cfb339fb5a5/tasks/training/task048.py#L69
p=lambda i,r=1,k=40:-k*[[8-8*("2"in str(i))]]or p([[(y>=1==s)or y-r+(r:=y!=2<r*3)for s,y in zip([0,*x],x)]for x in zip(*i[::-1])],0,k-1)