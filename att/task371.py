def p(a):
	b=sum(a,[]).index;c=b(1);d=b(1,c+1)+c>>1
	for i in[l:=len(a[0]),~l,1,1,~l]:d+=i;a[d//l][d%l]=3
	return a