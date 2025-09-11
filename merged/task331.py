# joking (84 vs 83 bytes for gold)
p=lambda i,k=7:-k*i or p(eval(str([*zip(*i[::-1])]).replace("1, ","1,86//k%1")),k-2)

### combined (86 bytes)
p=lambda i,k=7:-k*i or p(eval(str([*zip(*i[::-1])]).replace("1, 0","1,86//k%10")),k-2)
