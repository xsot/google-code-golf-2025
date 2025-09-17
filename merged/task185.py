# ovs (138 bytes, gold)
p=eval(('lambda i:'+'[[sum({r.pop()}&)r,r[1:])]*'*2+'[[r[0]r,*i)if]i if])])]').translate([0,"{*r}-{*i[0]}","zip(","for*r,in "]))

## without the `str.translate` compression:

exec('def p(i):h={*i[0]};return'+'[[a*({a}=={b}-h)for a,b in zip(r,r[1:])]for*r,in zip(*'*2+'[[t[0]for t in zip(s,*i)if{*t}-h]for s in i if{*s}-h])])]')

## idea for a shorter solution? Doesn't quite work, dealing with empty lines in the output is difficult.

def p(i):h={*i[0]};[i:=[[b*({w}=={w:=b}-h)for b,*C in zip(r,*i)if len({*C}&h)<2]for*r,in zip(*i)if{*r,w:=0}-h]for _ in'  '];return[r[1:]for r in i]

### combined (162 bytes)
p=lambda i:[[1//len(q:={*sum([[t[0]for t in zip(s,*i)if{*t,0}>h][y:y+2]for s in i if{*s,0}>(h:={*i[0]})][x:x+2],[])})*max(q-h|{0})for y in[0,1,2]]for x in[0,1,2]]
