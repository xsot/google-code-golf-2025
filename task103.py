p=lambda m:[[7**any(x^y for x,_,y in m)]]

##
p=lambda m:[[any(x^y for x,_,y in m)*7or 1]]
p=lambda m:[[any(l[0]!=l[2]for l in m)*7or 1]]
p=lambda m:[[(str(m)[2::11]!=str(m)[8::11])*7or 1]]