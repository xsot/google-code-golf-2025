# joking (95 vs 83 bytes for gold)
p=lambda i,z=0:[[z:=z+min(x)%5]*(c:=0)+[c-(c:=c-y)or~-b""[c%3+z]for y in x]for x in i]
# there's gotta be some pysearch for those constants
# z can start at an arbitray point, the increments for z and c can be adjusted
# maybe large number%(c%N+z) where c%N is even and z starts at an odd to increase the chances

### mwi (100 bytes)
p=lambda i,z=0:[[z:=z+1-((c:=0)in x)]and[-c+(c:=c+y)or b"020463010"[z*3+c%7]%8for y in x]for x in i]

### combined (104 bytes)
p=lambda i,z=0:[[z:=z+1-((c:=0)in x)]and[-c+(c:=c+y)or[0,2,0,4,6,3,0,1,0][z*3+c%7]for y in x]for x in i]
