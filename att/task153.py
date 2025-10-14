r=3,2,1;p=lambda g:max(({*str(w:=[[max(g[A%10-y][A%11-x]for A in(a,a%119))for x in r]for y in r])}^{'0'},w)for a in range(6666))[1]

##
s=' in[a '+'for*a,in map(zip,a[9:]+a,a,a[1:]+a)'*2;p=eval(f'lambda a:max(all(sum(d:=[[*map(int.__xor__,*e)]for*e,in zip(b,c)],a))*d for b{s}]for c{s}])')