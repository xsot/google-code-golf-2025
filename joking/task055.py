p=lambda i,z=0:[[z:=z+min(x)%5]*(c:=0)+[c-(c:=c-y)or~-b""[c%3+z]for y in x]for x in i]
# there's gotta be some pysearch for those constants
# z can start at an arbitray point, the increments for z and c can be adjusted
# maybe large number%(c%N+z) where c%N is even and z starts at an odd to increase the chances