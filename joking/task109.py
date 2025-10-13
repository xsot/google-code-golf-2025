p=lambda a:eval(f'[[a and{a[i:=len(a)//2]}[0]\nfor a in a[:{i}]+a[{i}-1::-1]]#'*2)

## recursive alt
p=lambda a,s=0:a*0!=0and[*map(p,a[:(l:=len(a)//2)]+a[l-1::-1],[a[l]]*29)]or a%~a&s