# mwi (100 vs 84 bytes for gold)
p=lambda i,z=0:[[z:=z+1-((c:=0)in x)]and[-c+(c:=c+y)or b"020463010"[z*3+c%7]%8for y in x]for x in i]

### combined (104 bytes)
p=lambda i,z=0:[[z:=z+1-((c:=0)in x)]and[-c+(c:=c+y)or[0,2,0,4,6,3,0,1,0][z*3+c%7]for y in x]for x in i]
