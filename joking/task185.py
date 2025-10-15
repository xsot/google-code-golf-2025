exec("p=lambda i,k=-1:[[sum({r[1]}&{r[0]}-{*i[0]})if k<1else r[1]"+"for*r,in %s)if{*r[1:]}-{*k*i[0]}]"*2%("zip(r[1:],r,*i","k*i or zip(*p(i,k+1)"))

## some rearrangements of the other solution
## slightly hampered by having no idea how the code works
p=lambda i,k=1:-k*[(r[0]for*r,in zip(r,*i)if{*r}-{*i[0]})for*r,in i if{*r}-{*i[0]}]or[[sum({r.pop()}&{*r}-{*i[0]})for*r,in zip(r,r[1:])]for*r,in zip(*p(i,k-1))]
p=lambda i,k=2:[[sum({r[1]}&{r[0]}-{*i[0]})if k else r[1]for*r,in zip(r[1:],r,*i)if k or{*r[1:]}-{*i[0]}]for*r,in(k<1)*i or zip(*p(i,k-1))if k or{*r}-{*i[0]}]
p=lambda i,k=-1:[[sum({r[1]}&{r[0]}-{*i[0]})if k<1else r[1]for*r,in zip(r[1:],r,*i)if{*r[1:]}-{*k*i[0]}]for*r,in k*i or zip(*p(i,k+1))if{*r}-{*k*i[0]}]
exec("p=lambda i,k=1:-k*[(r[0]\2zip(r,*i)if\1)\2i if\1]or[[sum({r.pop()}&\1)\2zip(r,r[1:])]\2zip(*p(i,k-1))]".translate([0,"{*r}-{*i[0]}","for*r,in "]))
exec("p=lambda i,k=1:-k*[(r[0]\2r,*i)if\1)\2*zip(*i))if\1]or[[sum({r.pop()}&\1)\2r,r[1:])]\2*p(i,k-1))]".translate([0,"{*r}-{*i[0]}","for*r,in zip("]))
exec("p=lambda i,k=1:-k*[(r[0]\2\3r,*i)if\1)\2i if\1]or[[sum({r.pop()}&\1)\2\3r,r[1:])]\2\3*p(i,k-1))]".translate([0,"{*r}-{*i[0]}","for*r,in ","zip("]))