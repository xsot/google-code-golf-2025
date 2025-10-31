# joking (168 vs 145 bytes for gold)
def p(a,n=3,i=0):
 for b in a:
  B=bytes(b+[0]).find;d=B(0,c:=B(b'\0')+1)+~c;i+=1
  for e in a[i+~d:i+d]:e[:c]=[e[c]]*c
 return-n*a or p([b[::-1]for*b,in zip(*a)],n-1)

### ovs (177 bytes)
def p(a,n=3,i=0):
 for b in a:
  B=bytes(b+[0]).find;d=B(0,c:=B(b'\0')+1)+~c;i+=1
  for e in a[i+~d:i+d]:e[:c]=[e[c]]*len(e[:c])
 return-n*a or p([b[::-1]for*b,in zip(*a)],n-1)

### att (182 bytes)
def p(a,n=3,i=0):
	for b in a:
		for e in a[i-(d:=[0,*b][(c:=bytes(b).find(b'\0'))::-1].index(0)):(i:=i+1)+d]:e[c:]=[e[c]]*len(e[c:])
	return-n*a or p([b[::-1]for*b,in zip(*a)],n-1)

### combined (182 bytes)
def p(a,n=3,i=0):
	for b in a:
		for e in a[i-(d:=[0,*b][(c:=bytes(b).find(b'\0'))::-1].index(0)):(i:=i+1)+d]:e[c:]=[e[c]]*len(e[c:])
	return-n*a or p([b[::-1]for*b,in zip(*a)],n-1)
