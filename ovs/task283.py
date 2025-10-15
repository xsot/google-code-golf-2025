p=lambda i,*w:i*0!=0and[*map(p,i,[i]+i,i[1:]+[i],*w)]or-i%8*w.count(5)%5

##
E=enumerate
p=lambda g:[[v*~sum(abs(j-J)+abs(i-I)==1for I,R in E(g)for J,V in E(R)if V)%8%5for j,v in E(r)]for i,r in E(g)]
