# ovs (83 vs 82 bytes for gold)
p=lambda i,k=2:k//9*i or p(eval(str([*zip(*i[::-1])]).replace("1,","1,k|")),k*9%11)

### joking (84 bytes)
p=lambda i,k=7:-k*i or p(eval(str([*zip(*i[::-1])]).replace("1, ","1,86//k%1")),k-2)

##
p=lambda i:[i:=eval(str([*zip(*i[::-1])]).replace("1, 0","1,"+k))for k in"2786"][3]
p=lambda i:[i:=eval(str([*zip(*i[::-1])]).replace("1,","1,k|"))for k in[2,7,8,6]][3]
p=lambda i:[i:=eval(str([*zip(*i[::-1])]).replace("1,",f"1,{k}|"))for k in"2786"][3]

##
p=lambda i,*w:i*0!=0and[*map(p,i,[i]+i,i[1:]+[i],*w)]or[1,6,7,8,2,0][[i,*w,1].index(1)]
p=lambda i,*w:i*0!=0and[*map(p,i,[i]+i,i[1:]+[i],*w)]or i or[6,7,8,2,0][[*w,1].index(1)]
p=lambda i,*w:i*0!=0and[*map(p,i,[i]+i,i[1:]+[i],*w)]or i or 7%(2-[*w,1].index(1)^4)+5
p=lambda i,*w:i*0!=0and[*map(p,i,i[1:]+[i],[i]+i,*w)]or[7,6,2,8,0][[*w,1].index(1)]+i
p=lambda i,*w:i*0!=0and[*map(p,i,[i]+i,i[1:]+[i],*w)]or b'\0'[[*w,1].index(1)]+i

## ties 83
p=lambda i:[i:=eval(str([*zip(*i[::-1])]).replace("1,","1,k|"))for k in b''][3]
p=lambda i,*w:i*0!=0and[*map(p,i,[i]+i,i[1:]+[i],*w)]or[6,7,8,2,i][[*w,1].index(1)]
p=lambda i,*w:i*0!=0and[*map(p,i,i[1:]+[i],[i]+i,*w)]or[7,6,2,8,i][[*w,1].index(1)]
p=lambda i,*w:i*0!=0and[*map(p,i,[i]+i,i[1:]+[i],*w)]or 7%(2-[*w,1].index(1)^4)+5+i
p=lambda i,*w:i*0!=0and[*map(p,i,[i]+i,i[1:]+[i],*w)]or 20%(10-[*w,1].index(1)^4)+i

### combined (86 bytes)
p=lambda i,k=7:-k*i or p(eval(str([*zip(*i[::-1])]).replace("1, 0","1,86//k%10")),k-2)
