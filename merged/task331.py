# combined (86 vs 2500 bytes for gold)
p=lambda i,k=7:-k*i or p(eval(str([*zip(*i[::-1])]).replace("1, 0","1,86//k%10")),k-2)
