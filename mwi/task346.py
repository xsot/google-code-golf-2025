p=lambda i:[max([n]for n in sum(i,[])if str(i).count(f"{n}, "*3)<2)]

##
p=lambda i:[[n for n in{*sum(i,[])}if n>str(i).count(f"{n}, "*3)<2]]
p=lambda i:[max([str(i).count(f"{n}, "*3)>1or n]for n in sum(i,[]))]