p=eval(f'lambda i:[[([i[a][b]]*4+[i{" for i in i[a-3:a]+i[a+3:a:-1]for a in[b]"*2}if i])[-4]'+'for %c in range(6)]'*2%(98,97))

##
import re;p=lambda a,n=-3:n*a or[*zip(*eval(re.sub(r'0(?=(, 0)?(.{20}){1,2}, ([^0]).{22}(?!\3|0)(.), 0)',r'\4',str(p(a,n+1)))))][::-1]