def p(i):g=sum(i,[]);z=len({*g})-1;r=range(5*z);u=z*0**g[5];v=z*0**g[1];return[[i[x//z][y//z]or(x-~y==v+u+z*2or x-y==v-u)*2for y in r]for x in r]

##
def p(i):g=sum(i,[]);z=len({*g})-1;r=range(5*z);return[[i[s:=x//z][t:=y//z]or(g[(t-s)%6::6].count(f:=i[1][1])>1==x%z-y%z+1or x%z+y%z==z*g[(t+s)%5::4].count(f)+~z)*2for y in r]for x in r]
def p(i):g=sum(i,[]);z=len({*g})-1;r=range(5*z);return[[i[s:=x//z][t:=y//z]or((x-y)%z<1<g[(t-s)%6::6].count(f:=i[1][1])or(x+y)%z==z*g[(t+s)%5::4].count(f)+~z)*2for y in r]for x in r]
def p(i):g=sum(i,[]);z=len({*g})-1;r=range(5*z);return[[i[s:=x//z][t:=y//z]or((x-y)%z<1<g[(t-s)%6::6].count(f:=i[1][1])or~(x+y)%z<1<g[(t+s)%5::4].count(f))*2for y in r]for x in r]
def p(i):g=sum(i,[]);z=len({*g})-1;r=range(5*z);return[[i[s:=x//z][t:=y//z]or(g[(t-s)%6::6].count(f:=i[1][1])>>(x-y)%z|g[(t+s)%5::4].count(f)>>(x-~y)%z)&2for y in r]for x in r]
exec(('def p(i):g=sum(i,[]);z=len({*g})-1;return[[i[x//z][y//z]'+'or g[(y%sx)//z%%%s::%s].count(g[6])>>(x-%sy)%%z&2'*2+'for %s in range(5*z)]'*2)%(*'-66++54~yx',))