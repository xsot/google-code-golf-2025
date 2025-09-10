p=lambda a:a>a*0!=0and[p(a[0])]*2+p(a[1:])or a

##

r=lambda w:sum([[x]*2for x in w],[]);p=lambda g:r(map(r,g))
