# joking (82 vs 81 bytes for gold)
p=lambda a:eval(f'[[a and{a[i:=len(a)//2]}[0]\nfor a in a[:{i}]+a[{i}-1::-1]]#'*2)

### att (83 bytes)
p=lambda a:eval('[[a and%s[0]'%a[i:=len(a)//2]+f'for a in a[:{i}]+a[{i}-1::-1]]'*2)

### combined (91 bytes)
def p(i):t=len(i)//2;return[[y and x[t]for y in x[:t]+x[t-1::-1]]for x in i[:t]+i[t-1::-1]]
