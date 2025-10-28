import re;p=lambda g,k=9:-k*g or p(eval(re.sub(r"(?<=(.).{28})(?=(.{29})+\1)0",r"\1",str(g)))[::-1],k-1)

##
import re;p=lambda g,k=9:-k*g or p(eval(re.sub(r"(?<=(.).{34})(?=(.{35})+\1)0",r"\1",str(g)))[::-1],k-1)
import re;p=lambda g:exec(r'g[::-1]=eval(re.sub(r"(?<=(.).{34})(?=(.{35})+\1)0",r"\1",str(g)));'*10)or g