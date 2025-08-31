p=lambda i:[max([n]for n in sum(i,[])if str(i).count(f"{n}, "*3)<2)]

##
p=lambda i:[max((str(i).count(f"{n}, "*3)<2)*[n]for n in sum(i,[]))]
p=lambda i:[[n]for n in{*sum(i,[])}if(str(i).count(f"{n}, "*3)<2)*n]