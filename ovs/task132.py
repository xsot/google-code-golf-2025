p=lambda i,v=0:[i:=[[v|(v:=v^sum({*A}&{*y}))for A in i]for y in zip(*i)]for _ in i][1]
