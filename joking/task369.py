p=lambda g,k=-11,z=1:k*g or[[P:=v&7or[z:=z*8,4-v%7,P&~5|v][k>>3]for v in[5]+r][:0:-1]for*r,in zip(*p(g,k+1))]

##
p=lambda g,k=10,z=1:~k*g or[[P:=v&7or[P&~5|v,4-v%7,z:=z*8][k//9]for v in[5]+r][:0:-1]for*r,in zip(*p(g,k-1))]
p=lambda g,k=10,z=1:~k*g or[[P:=v&7or[P&~5|v,4-v%7,z:=z*8][k>>3]for v in[5]+r][:0:-1]for*r,in zip(*p(g,k-1))]