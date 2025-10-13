# joking (82 vs 80 bytes for gold)
p=lambda a:eval(f'[[a and{a[i:=len(a)//2]}[0]\nfor a in a[:{i}]+a[{i}-1::-1]]#'*2)

## recursive alt
p=lambda a,s=0:a*0!=0and[*map(p,a[:(l:=len(a)//2)]+a[l-1::-1],[a[l]]*29)]or a%~a&s

### att (83 bytes)
p=lambda a:eval('[[a and%s[0]'%a[i:=len(a)//2]+f'for a in a[:{i}]+a[{i}-1::-1]]'*2)

### combined (91 bytes)
def p(i):t=len(i)//2;return[[y and x[t]for y in x[:t]+x[t-1::-1]]for x in i[:t]+i[t-1::-1]]
