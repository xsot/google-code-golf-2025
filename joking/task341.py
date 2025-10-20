p=lambda i:[i:=[[b[a]or(v:=2+({*s}>{*s[a:]}>{0}and v))&8for b,s in zip(i,i[1:]+i)]for a in range(10)]for r in i][1]

##
p=lambda i:[i:=[[i[b][a]or all(len({*s[b:]})%len({*s})&2for s in[*zip(*i)][a+a%~a:a+2])*8for b in r]for a in r]for r in[range(10)]*2][1]