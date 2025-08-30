# att (122 vs 117 bytes for gold)
z=[[0]*10]
p=lambda a:eval(f'[[[0,2,2,*a[1]][[*map("{a}".count,str(a))].count(1)]'+'for*a,in map(zip,z+a,a,a,a[1:]+z)]'*2)

### joking+mwi (157 bytes)
p=lambda i,k=range(10):[[(l:=min(h:=sum(i,[]),key=h.count))in sum([z[y-(y>0):y+2]for z in i[x-(x>0):x+2]],[])and(i[x][y]==l and l or 2)for y in k]for x in k]
