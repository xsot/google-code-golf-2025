p=lambda a,m=9:[*zip(*{(d,)*m:0for d in sum(zip(*a),())if sum(a,[]).count(d)==m})]or p(a,m-1)
