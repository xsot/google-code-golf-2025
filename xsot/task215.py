p=lambda m,i=0:m[i:]and[max(m[i%3::3])]+p(m,i+1)
##
p=lambda m:[max(m[i%3::3])for i in range(len(m))]