# att (77 bytes, gold)
p=lambda a,s=0:a*0!=0and(b:=[*map(p,a,[a[l:=len(a)//2]]*l)])+b[::-1]or a%~a&s

### joking (82 bytes)
p=lambda a:eval(f'[[a and{a[i:=len(a)//2]}[0]\nfor a in a[:{i}]+a[{i}-1::-1]]#'*2)

## recursive alt
p=lambda a,s=0:a*0!=0and[*map(p,a[:(l:=len(a)//2)]+a[l-1::-1],[a[l]]*29)]or a%~a&s

### combined (91 bytes)
def p(i):t=len(i)//2;return[[y and x[t]for y in x[:t]+x[t-1::-1]]for x in i[:t]+i[t-1::-1]]
