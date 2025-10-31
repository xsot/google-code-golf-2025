# ovs (84 vs 83 bytes for gold)
p=lambda g:[max([[-x^-y<1and(x|y)for x,y in zip(b,a)]for a in g],key=all)for b in g]

### mwi (105 bytes)
# If you find a golf for this hole, try applying it to task017
p=lambda g,k=-1:k*g or p([*zip(*[max(a for a in g if all(x in[0,y]for x,y in zip(b,a)))for b in g])],k+1)

## Only fails one testcase
p=lambda g:[max(a for a in g if all(x in[0,y]for x,y in zip(b,a)))for b in g]

### att (132 bytes)
p=lambda a,i=1:9<sum(b[i:]==b[:-i]for b in zip(*a))and[[c:=[*map(max,*a[j%i::i])],c[9:]+c[-9:]][0in c]for j in range(29)]or p(a,i+1)

### combined (188 bytes)
def p(i,A=range(29)):J,a=[[K+1for K in A if all(len({*w[b::K+1],0})<3for w in l for b in A)][0]for l in[i,zip(*i)]];return[[max(sum([s[y%J::J]for s in i[x%a::a]],[]))for y in A]for x in A]
