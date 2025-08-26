p=lambda x:(x+x[1:-1])*2+x[:1]
##
p=lambda x:(x+x[1:-1])*2+[x[0]]
p=lambda x:(y:=x+x[::-1][1:])+y[1:]