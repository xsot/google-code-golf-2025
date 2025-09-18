p=lambda i:[b:=sum(i,[]),*filter(any,zip(*sorted([c:=-b.count(e),e]*-c+[0]*22for e in{*b})))][2::2]

##
p=lambda i:[b:=sum(i,[]),*filter(any,zip(*sorted({(e,~e)*b.count(e)+(0,)*99for e in b},key=sum)))][1::2]