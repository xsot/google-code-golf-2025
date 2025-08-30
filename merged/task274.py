# xsot (77 vs 71 bytes for gold)
p=lambda m:[[*[8]*(c:=str(m).count("0, 5, 0")//2),0,0][:3],[0,0,4+c&8],[0]*3]
##
p=lambda m:[[*[8]*(c:=str(m).count("0, 5, 0")//2),0,0][:3],[0,0,c//4*8],[0]*3]
