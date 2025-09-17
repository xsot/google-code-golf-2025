def	p(I):
	for	n	in	2,3:
		z,t,T,*R=[{(l,n)for	l,I	in	enumerate(I)for	n,I	in	enumerate(I)if	I>=C}for	C	in(0,2,5,7)]
		for	d,i	in	z:v={(l,I)for	l,I	in	z	if	abs(d-l+(i-I)*1j)in(0,2,1,n)};R+=[l|v	for	l	in	R	if	t-l>v]
		for	l	in	R:
			if	t-T<l:
				for	l,n	in	l&T:I[l][n]=8
				return	I

##
def p(i,n=2):
 s=*range(-n,0),*range(1,n+1);z=*zip(s,z:=[0]*9),*zip(z,[*s,0]);f=eval(str(i))
 for x in range(30):
  for y in range(len(i[0])):
   for a,b in zip((min(t:=[1-(len(i[0])>y+b>-1<x+a<len(i))or i[x+a][y+b]for a,b in z])*(n+1<t.count(2)//3*~t[:n*2].count(2)*~t[n*2:-1].count(2)or n==t[0]==t[3]or n>2==t[6]==t[8]))*z,t):f[x+1%b*a[0]][y+1%b*a[1]]=~b&9
 return"2"in str(f)and p(i,n+1)or eval(str(f).replace(*"92"))