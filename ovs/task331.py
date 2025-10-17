p=lambda i,k=2:k//9*i or p(eval(str([*zip(*i[::-1])]).replace("1,","1,k|")),k*9%11)
