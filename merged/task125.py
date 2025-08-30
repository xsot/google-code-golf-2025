# joking+mwi (156 vs 126 bytes for gold)
p=lambda i,k=11,r=range(15):-k*i or p([[(y:=i[~b][a])*(y%6%4<1)or(i[-b][a]==4or i[~b][a-1]&i[-b][a]==6)*4or(i[-b][a-1]==6)*3or y for b in r]for a in r],k-1)
