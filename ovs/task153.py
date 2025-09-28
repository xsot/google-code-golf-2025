r=-1,0,1
p=lambda g:max(({*str(w:=[[max(g[(y+A)%10][(x+A//10)%10]for A in(a,a%99))for x in r]for y in r])}^{'0'},w)for a in range(5000))[1]
