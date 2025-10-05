def p(g):
 A=[[*H]for H in zip(*g)if 1in H]
 A=[[*H]for H in zip(*A)if 1in H]
 for H in 0,1,0,1,0,1,0,1:g=H*g[::-1]or[[*H]for H in zip(*g)];[0for C,H in enumerate(g,-1)for D,H in enumerate(g,-1)for F,H in enumerate(all(g[C+F][D+G]==H&-2if-1<D+G<23>C+F>-1else H<4for F,H in enumerate(A)for G,H in enumerate(H))*A)for G,H in enumerate(H)if-1<D+G<23>C+F>-1for g[C+F][D+G]in[H]]
 return g

##
def p(g):
 A=[[*H]for H in zip(*g)if 1in H]
 A=[[*H]for H in zip(*A)if 1in H]
 for H in#['[0,1]*4','[0,1]*8',' 0,1,0,1,0,1,0,1']##:g=H*g[::-1]or[[*H]for H in zip(*g)];[#[*range(10)]##for C,H in enumerate(g,-1)for D,H in enumerate(g,-1)for F,H in enumerate(all(g[C+F][D+G]==H&-2if-1<D+G<23>C+F>-1else H<4for F,H in enumerate(A)for G,H in enumerate(H))*A)for G,H in enumerate(H)if-1<D+G<23>C+F>-1for g[C+F][D+G]in[H]]
 return g