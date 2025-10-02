p=lambda i,k=79,z=1:-k*i or p([(e:=0)or[e:=y and[(y<6)*(z:=z*8)or e|y,y%7//6+1][k<1]for y in x]for x in zip(*i[::-1])],k-1)

## 
p=lambda i,k=79,z=1:-k*i or p([(e:=0)or[e:=y and[(y<6)*(z:=z*8)|e|y,(y%7==4)+1][k<1]for y in x]for x in zip(*i[::-1])],k-1)