# ovs (119 vs 98 bytes for gold)
E=enumerate
p=lambda g:[[v+sum(V*-V&7for I,R in E(g,-i)for J,V in E(R,-j)if I*I+J*J==V)for j,v in E(r)]for i,r in E(g)]
