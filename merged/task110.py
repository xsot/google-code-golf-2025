# combined (188 vs 109 bytes for gold)
def p(i,A=range(29)):J,a=[[K+1for K in A if all(len({*w[b::K+1],0})<3for w in l for b in A)][0]for l in[i,zip(*i)]];return[[max(sum([s[y%J::J]for s in i[x%a::a]],[]))for y in A]for x in A]
