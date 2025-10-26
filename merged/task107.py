# joking (140 bytes, gold)
def p(i):z=len({*str(i)})-5;r=range(5*z);u=z*0**i[1][0];v=z*0**i[0][1];return[[i[x//z][y//z]or(x-v in[z*2+u+~y,y-u])*2for y in r]for x in r]

##
def p(i):g=sum(i,[]);z=len({*g})-1;r=range(5*z);return[[i[s:=x//z][t:=y//z]or(g[(t-s)%6::6].count(f:=i[1][1])>1==x%z-y%z+1or x%z+y%z==z*g[(t+s)%5::4].count(f)+~z)*2for y in r]for x in r]
def p(i):g=sum(i,[]);z=len({*g})-1;r=range(5*z);return[[i[s:=x//z][t:=y//z]or((x-y)%z<1<g[(t-s)%6::6].count(f:=i[1][1])or(x+y)%z==z*g[(t+s)%5::4].count(f)+~z)*2for y in r]for x in r]
def p(i):g=sum(i,[]);z=len({*g})-1;r=range(5*z);return[[i[s:=x//z][t:=y//z]or((x-y)%z<1<g[(t-s)%6::6].count(f:=i[1][1])or~(x+y)%z<1<g[(t+s)%5::4].count(f))*2for y in r]for x in r]
def p(i):g=sum(i,[]);z=len({*g})-1;r=range(5*z);return[[i[s:=x//z][t:=y//z]or(g[(t-s)%6::6].count(f:=i[1][1])>>(x-y)%z|g[(t+s)%5::4].count(f)>>(x-~y)%z)&2for y in r]for x in r]
exec(('def p(i):g=sum(i,[]);z=len({*g})-1;return[[i[x//z][y//z]'+'or g[(y%sx)//z%%%s::%s].count(g[6])>>(x-%sy)%%z&2'*2+'for %s in range(5*z)]'*2)%(*'-66++54~yx',))
exec(('def p(i):g=sum(i,[]);z=len({*g})-1;return[[i[x//z][y//z]'+'or(x-%sy==z*0**g[1]%sz*0**g[5]+z%sz)*2'*2+'for %s in range(5*z)]'*2)%(*'~+++--yx',))
exec(('def p(i):g=sum(i,[]);z=len({*g})-1;return[[i[x//z][y//z]'+'or(x-%sy==z*(0**g[1]%s0**g[5]+%s))*2'*2+'for %s in range(5*z)]'*2)%(*'~+2+-0yx',))
exec(('def p(i):z=len({*str(i)})-5;return[[i[x//z][y//z]'+'or(x-%sy==z*(0**i[0][1]%s0**i[1][0]+%s))*2'*2+'for %s in range(5*z)]'*2)%(*'~+2+-0yx',))
def p(i):g=sum(i,[]);z=len({*g})-1;r=range(5*z);u=z*0**g[5];v=z*0**g[1];return[[i[x//z][y//z]or(x-~y==v+u+z*2or x-y==v-u)*2for y in r]for x in r]
def p(i):z=len({*str(i)})-5;r=range(5*z);u=z*0**i[1][0];v=z*0**i[0][1];return[[i[x//z][y//z]or(x-~y==v+u+z*2or x-y==v-u)*2for y in r]for x in r]

### ovs (165 bytes)
exec(('def p(i):g=sum(i,[]);z=len({*g})-1;return[[i[x//z][y//z]or 0'+'|g[(y%sx)//z%%%s::%s].count(g[6])>>(x-%sy)%%z&2'*2+'for %s in range(5*z)]'*2)%(*'-66++54~yx',))

### combined (194 bytes)
p=lambda i,r=range:(z:=len({*(g:=sum(i,[]))})-1)and[[i[s:=x//z][t:=y//z]or(g[(t-s)%6::6].count(f:=i[1][1])>1==x%z-y%z+1or g[(t+s)%5::4].count(f)>1==x%z+y%z-z+2)*2for y in r(5*z)]for x in r(5*z)]
