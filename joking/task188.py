p=lambda a,s=4:a[:s]*(a[:s]*2==a)or[*zip(*p([*zip(*a)],~-s%5))]

##
def p(a):A=*zip(*a),;c=A[:len(A)//2];return*zip(*c*(A==c*2)or p(A)),
p=lambda a,s=7:(h:=a[:s//2])*(h*2==a)or[*zip(*p([*zip(*a)],s-1))]
p=lambda a,s=4:a[:s%5]*(a[:s%5]*2==a)or[*zip(*p([*zip(*a)],s-1))]
p=lambda a,s=4:(h:=a[:s])*(h*2==a)or[*zip(*p([*zip(*a)],~-s%5))]