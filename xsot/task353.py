def p(m):a=sum(m,[]).index;R,C=divmod(a(4),N:=len(m[0]));m[r:=a(3)//N][c:=a(3)%N]=0;m[r+(R>r)-(R<r)][c+(C>c)-(C<c)]=3;return m

###
# att's
# i = current row
# i+=1 until we find the row with green
# if the yellow appeared in an earlier row, extract the row just before the green and put it at the end
# otherwise, this is the wrong orientation so we rotate and reset i
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