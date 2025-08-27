p=lambda a,n=-3,i=0:n*a or 3in a[i]and p([*zip(a.pop(('4'in'%s'%a[:i])*i-1),*a[::-1])],n+1)or p(a,n,i+1)

### xsot (229 bytes)
def p(m):a=sum(m,[]).index;R,C=divmod(a(4),N:=len(m[0]));m[r:=a(3)//N][c:=a(3)%N]=0;m[r+(R>r)-(R<r)][c+(C>c)-(C<c)]=3;return m
p=lambda a,n=-3,i=0:n*a or 3in a[i]and p([*zip(a.pop(('4'in'%s'%a[:i])-1),*a[::-1])],n+1)or p(a,n,i+1)

###
# att's
# i = current row with green
# find i, check if 4 appears in a[:i]
p=lambda a,n=-3,i=0:n*a or 3in a[i]and p([*zip(a.pop(('4'in'%s'%a[:i])*i-1),*a[::-1])],n+1)or p(a,n,i+1)

##
def p(m):
    find_coords = lambda val: next(
        (r, c) for r, row in enumerate(m) for c, v in enumerate(row) if v == val
    )
    r3, c3 = find_coords(3)
    r4, c4 = find_coords(4)
    dr, dc = r4 - r3, c4 - c3
    m[r3][c3] = 0
    m[r3 + (dr > 0) - (dr < 0)][c3 + (dc > 0) - (dc < 0)] = 3
    return m
