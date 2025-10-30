def p(n):
 r={e+u*1j:n for u,n in enumerate(n)for e,n in enumerate(n)};i,f=[u for u in r if r[u]==3]
 o=[(i,f-i,1),(i,i-f,1)]
 for*j,u,i,f in o:
  if(u in r)*f%8:
   if r[u]==2:return[[n|(e+u*1jin j)*3for e,n in enumerate(n)]for u,n in enumerate(n)]
   t=r[u]//8;o+={(*j,u-t*i,u-t*i+i*1j**e,i*1j**e,~t*f)for e in(t,-t)}