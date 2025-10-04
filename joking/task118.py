# version using complex numbers
def p(I):
 for n in(2,3):
  t,z,T,*R=[{l*1j+N for l,I in enumerate(I)for N,I in enumerate(I)if I>=n}for n in(2,0,5,6)]
  for d in z:v={l for l in z if abs(d-l)in(2,0,1,n)};R+=[l|v for l in R if t-l>v]
  for l in R:
   if t-T<l:
    for d in l&T:I[int(d.imag)][int(d.real)]=8
    return I