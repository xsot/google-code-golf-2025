p=lambda g,l=128:-l*g or p([*zip(*(a:=eval(str(g).replace(l//12*"5, ",l//12*"4>>l%3,"))))][::-1],l-3+(g>a))

##
p=lambda g,i=5,l=39:-l*g or p([*zip(*(a:=eval(str(g).replace(l//4*"5, ",l//4*"16%i,"))))][::-1],i+(g>a),l-1)
p=lambda g,l=172:-l*g or p([*zip(*(a:=eval(str(g).replace(l//16*"5, ",l//16*"~l*2%8%5,"))))][::-1],l-4+(g>a))