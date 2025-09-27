p=lambda i,n=-1,s=3:(r:=[(k//2*n*[0]+i[k%s])[:10]for k in range(10)])*(r[:5]==i[:5])or p(i,n+1,2)

##
# Surely there is a shorter way than `sum(i[2][k:]==i[0][:-k]for k in(1,2,2))` to count how many
# more 0s i[2] has in front than i[0]? If this can be done in <=20 bytes, it'd beat the above solution
p=lambda i:[((w:=i[4]!=i[1])*k//2*sum(i[2][k:]==i[0][:-k]for k in(1,2,2))*[0]+i[k%(3-w)])[:10]for k in range(10)]

p=lambda i,n=0:(r:=[(k//2*n*[0]+i[k%(3-(i[1]!=i[4]))])[:10]for k in range(10)])*(r[:5]==i[:5])or p(i,n+1)
