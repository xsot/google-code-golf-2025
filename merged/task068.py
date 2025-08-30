# joking+mwi (157 vs 117 bytes for gold)
p=lambda i,k=range(10):[[(l:=min(h:=sum(i,[]),key=h.count))in sum([z[y-(y>0):y+2]for z in i[x-(x>0):x+2]],[])and(i[x][y]==l and l or 2)for y in k]for x in k]
