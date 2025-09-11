def p(I):
 for n in 2,3:
  z,t,T,*R=[{(l,n)for l,I in enumerate(I)for n,I in enumerate(I)if I>=C}for C in(0,2,5,7)]
  for d,i in z:v={(l,I)for l,I in z if abs(d-l+(i-I)*1j)in{0,1,2,n}};R+=[l|v for l in R if t-l>v]
  for l in R:
   if t-T<l:
    for l,n in l&T:I[l][n]=8
    return I