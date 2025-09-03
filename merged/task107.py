# joking (186 vs 170 bytes for gold)
def p(i):g=sum(i,[]);z=len({*g})-1;r=range(5*z);return[[i[s:=x//z][t:=y//z]or(g[(t-s)%6::6].count(f:=i[1][1])>1==x%z-y%z+1or x%z+y%z==z*g[(t+s)%5::4].count(f)+~z)*2for y in r]for x in r]

### combined (194 bytes)
p=lambda i,r=range:(z:=len({*(g:=sum(i,[]))})-1)and[[i[s:=x//z][t:=y//z]or(g[(t-s)%6::6].count(f:=i[1][1])>1==x%z-y%z+1or g[(t+s)%5::4].count(f)>1==x%z+y%z-z+2)*2for y in r(5*z)]for x in r(5*z)]
