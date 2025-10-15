def p(g):
 A=[[*H]for H in zip(*g)if 1in H]
 A=[[*H]for H in zip(*A)if 1in H]
 for H in 0,1,0,1,0,1,0,1:g=H*g[::-1]or[[*H]for H in zip(*g)];[1for C,H in enumerate(g)for D,H in enumerate(g)for F,H in enumerate(all(g[C+F-1][D+G-1]==H&-2if 0<D+G<24>C+F>0else H<4for F,H in enumerate(A)for G,H in enumerate(H))*A)for G,H in enumerate(H)if 0<D+G<24>C+F>0for g[C+F-1][D+G-1]in[H]]
 return g

##
def p(g):
 A=[[*H]for H in zip(*g)if 1in H]
 A=[[*H]for H in zip(*A)if 1in H]
 for H in#['[0,1]*4','[0,1]*8',' 0,1,0,1,0,1,0,1']##:g=H*g[::-1]or[[*H]for H in zip(*g)];[#[*range(10)]##for C,H in enumerate(g)for D,H in enumerate(g)for F,H in enumerate(all(g[C+F-1][D+G-1]==H&-2if 0<D+G<24>C+F>0else H<4for F,H in enumerate(A)for G,H in enumerate(H))*A)for G,H in enumerate(H)if 0<D+G<24>C+F>0for g[C+F-1][D+G-1]in[H]]
 return g