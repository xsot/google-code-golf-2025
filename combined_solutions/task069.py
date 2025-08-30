def p(i):
 q=sum(1for x in zip(*i)if{*x}-{0,8})-1;s=sum(i,[]);r=*range(len(m:=[y*(y!=8)for x in i for y in x if{*x}-{0,8}])),;z=-8
 while z<99:
  g=all(sum(s[n+z:][:1])for n in r if m[n])
  for l in r*g:
   if m[l]:t=z+l;i[t//10][t%10]=m[l]*(s[t]==8)
  z+=q*g+1
 return i