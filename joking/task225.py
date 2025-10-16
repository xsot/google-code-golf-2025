# alt. i think there might be some way to rearrange this to save a byte or two
p=eval(f'lambda i:[[max([i[c:=a][b]]+[i{" for i in i[c-3:c]+i[c+3:c:-1]if(c:=b)*i+i"*2}][:-3])'+'for %c in range(6)]'*2%(98,97))

##
p=eval(f'lambda i:[[max([i{" for i in i[%s-3:%s]+i[%s+3:%s:-1]"*2}if i][:-3]+[i[a][b]]){"for %s in range(6)]"*2}'%(*'aaaabbbbba',))
p=eval("lambda i:[[max([i\nfor i in i[a-3:a]+i[a+3:a:-1]for a in[b]#"*2+'\nif i][:-3]+[i[a][b]])'+'for %c in range(6)]'*2%(98,97))
p=eval(f'lambda i:[[max([i[a][b]]+[i{" for i in i[%s-3:%s]+i[:%s:-1][-3:]"*2}if i][:-3]){"for %s in range(6)]"*2}'%(*'aaabbbba',))
p=eval(f'lambda i:[[max([i[c:=a][b]]+[i{" for i in i[c-3:c]+i[c+3:c:-1]if[c:=b]and i"*2}][:-3])'+'for %c in range(6)]'*2%(98,97))
p=eval(f'lambda i:[[max([i[c:=a][b]]+[i{" for i in i[c-3:c]+i[c+3:c:-1]if-~(c:=b)*i"*2}][:-3])'+'for %c in range(6)]'*2%(98,97))

p=lambda i,r=range(6):[[max([s for t in i[a-3:a]+i[a+3:a:-1]for s in t[b-3:b]+t[b+3:b:-1]if s][:-3]+[i[a][b]])for b in r]for a in r]