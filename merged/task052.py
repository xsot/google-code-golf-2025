# att (41 vs 40 bytes for gold)
p=lambda a:[3*[1//len({*b})*5]for b in a]

### joking (tied, 41 bytes)
p=lambda a:[3*[(b==b[:1]*3)*5]for b in a]

##
p=lambda a:[3*[1//len({*b})*5]for b in a]
p=lambda a:[3*[(r==[b]*2)*5]for*r,b in a]
p=lambda a:[3*[(r==[b,b])*5]for*r,b in a]
p=lambda a:[3*[[*{*b},0,0,5][3]]for b in a]
p=lambda a:[3*[({*b}=={b[0]})*5]for b in a]
p=lambda a:[3*[(b[0]==b[1]==b[2])*5]for b in a]
p=lambda a:[3*[(b[:2]==b[1:])*5]for b in a]
p=lambda a:[3*[(b==[*{*b}]*3)*5]for b in a]
p=lambda a:[3*[min(b)//max(b)*5]for b in a]
p=lambda a:[3*[(s==t==u)*5]for s,t,u in a]
p=lambda a:[3*[({*r}=={b})*5]for*r,b in a]
p=lambda a:[3*[(sum(b)==b[0]*3)*5]for b in a]

### mwi (tied, 41 bytes)
p=lambda a:[3*[5*(b==b[:1]*3)]for b in a]

##

p=lambda a:[3*[1//len({*b})*5]for b in a]
p=lambda a:[3*[5*(a==[b]*2)]for*a,b in a]
p=lambda a:[3*[5*(x==y==z)]for x,y,z in a]
p=lambda a:[3*[len({*b})%3%2*5]for b in a]
p=lambda a:[3*[5*({*a}=={b})]for*a,b in a]
p=lambda a:[3*[5*(sorted(a)==a)]for a in a]

### ovs (tied, 41 bytes)
p=lambda g:[3*[1//len({*r})*5]for r in g]

### xsot (tied, 41 bytes)
p=lambda m:[3*[1//len({*r})*5]for r in m]

##
p=lambda m:[3*[5*(len({*r})<2)]for r in m]

### combined (tied, 41 bytes)
p=lambda g:[3*[1//len({*A})*5]for A in g]
