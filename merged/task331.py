# ovs (83 bytes, gold)
p=lambda i,k=2:k//9*i or p(eval(str([*zip(*i[::-1])]).replace("1,","1,k|")),k*9%11)

### joking (84 bytes)
p=lambda i,k=7:-k*i or p(eval(str([*zip(*i[::-1])]).replace("1, ","1,86//k%1")),k-2)


##
p=lambda i,*w:i*0!=0and[*map(p,i,i[:1]+i,i[1:]+i[-1:],*w)]or[1,6,7,8,2,0][[i,*w,1].index(1)]
p=lambda i,*w:i*0!=0and[*map(p,i,i[:1]+i,i[1:]+i[-1:],*w)]or i or[6,7,8,2,0][[*w,1].index(1)]
p=lambda i,*w:i*0!=0and[*map(p,i,i[:1]+i,i[1:]+i[-1:],*w)]or i or 7%(2-[*w,1].index(1)^4)+5

p=lambda i,*w:i*0!=0and[*map(p,i,i[:1]+i,i[1:]+i[-1:],*w)]or b'\0'[[i,*w,1].index(1)]

### combined (86 bytes)
p=lambda i,k=7:-k*i or p(eval(str([*zip(*i[::-1])]).replace("1, 0","1,86//k%10")),k-2)
