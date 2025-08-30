# ovs (110 vs 84 bytes for gold)
p=lambda g:[*zip(*[*[(P:=[0]*~-(h:=len(g)))*h]*(m:=max(g)).index(c:=max(m)),*[C:=[c]*h,[5]+P,C,P+[5]]*h][:h])]
