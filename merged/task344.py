# combined (78 bytes, gold)
p=lambda i,k=3:-k*i or[*zip(*eval(str(p(i,k-1)[::-1]).replace("2, 3","0,8")))]
