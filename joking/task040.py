p=lambda i,c=9:[[(y>0)*i[59-(c:=c+1)>>9][c//5%-2]for y in x]for x in i]


##
p=lambda i,E=enumerate:[[y and i[-(a>4)][-(b>4)]for b,y in E(x)]for a,x in E(i)]
p=lambda i,r=range(10):[[i[a][b]and i[-(a>4)][-(b>4)]for b in r]for a in r]
p=lambda i,c=9:[[(y>0)*i[-((c:=c+1)>59)][-(c%10>4)]for y in x]for x in i]
p=lambda i,c=9:[[(y>0)*i[59-(c:=c+1)>>9][c//5%-2]for y in x]for x in i]