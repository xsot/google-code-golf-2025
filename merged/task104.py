# ovs (116 vs 84 bytes for gold)
Q=[0]
p=lambda g:[Q*9][(t:=g[0][1]>0):]+([Q[(f:=g[1][0]>0):]+(H:=[3]*4+Q*f)+Q*4]*4+[Q*(5-f)+H]*4)[::-t^-f|1]+[Q*9]*t
