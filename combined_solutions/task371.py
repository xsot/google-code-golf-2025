def p(a):
	b=sum(a,[]).index;d=b(1,b(1)+1)+b(1)>>1
	for i in[l:=len(a[0]),~l,1,1,~l]:d+=i;a[d//l][d%l]=3
	return a