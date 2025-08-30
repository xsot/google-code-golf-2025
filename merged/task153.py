# joking+mwi (184 vs 175 bytes for gold)
def p(g,R=range):u=[[(r*2)[x:x+3]for r in(g*2)[y:y+3]]for x in R(10)for y in R(10)];return[t for a in u for b in u if"0"not in str(t:=[[a[y][x]^b[y][x]for x in R(3)]for y in R(3)])][0]
