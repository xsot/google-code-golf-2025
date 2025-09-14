p=lambda a:[*zip(*(c:=(A:=[*zip(*a)])[:len(A)//2])*(A==c*2)or p(A))]
