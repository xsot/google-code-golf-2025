# att (245 (251 unzipped) vs 153 bytes for gold)
def p(a):
	f=lambda b:[c for*c,in zip(*b)if{*c}-{0,8}];s=f(f(a));n=len(s[0])
	for i in range(99):
		j=i%10;i//=10;t=[c[j:j+n]for c in a[i:i+len(s)]]
		for c,d in zip(s,a[i:]*(t in[s,[[d and 8for d in c]for c in s]])):d[j:j+n]=c*(t!=s)or[0]*n
	return a

### joking+mwi (251 bytes)
def p(a):
	f=lambda b:[c for*c,in zip(*b)if{*c}-{0,8}];s=f(f(a));n=len(s[0])
	for i in range(99):
		j=i%10;i//=10;t=[c[j:j+n]for c in a[i:i+len(s)]]
		for c,d in zip(s,a[i:]*(t in[s,[[d and 8for d in c]for c in s]])):d[j:j+n]=c*(t!=s)or[0]*n
	return a
