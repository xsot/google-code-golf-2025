# att (132 vs 85 bytes for gold)
p=lambda a,i=1:9<sum(b[i:]==b[:-i]for b in zip(*a))and[[c:=[*map(max,*a[j%i::i])],c[9:]+c[-9:]][0in c]for j in range(29)]or p(a,i+1)

### combined (188 bytes)
def p(i,A=range(29)):J,a=[[K+1for K in A if all(len({*w[b::K+1],0})<3for w in l for b in A)][0]for l in[i,zip(*i)]];return[[max(sum([s[y%J::J]for s in i[x%a::a]],[]))for y in A]for x in A]
