r=range(324)
def p(a):
	for i in r:
		b=a[i%18:][:3];i//=18;z=any(max([*zip(*b)][i:i+3]))
		for k in r:b[k%5%3][i+k%3]**=z
	return a