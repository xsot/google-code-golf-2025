# att (133 vs 129 bytes for gold)
def p(g):f=sum(g,[]);return[[(i:=j-71)*0+max(v*(f[(i:=i+1):i+2]==[v,v])for v in f)for j in R]for R in b"9988 9``8 S``R SSRR".split()]

### xsot (136 bytes)
def p(g):f=sum(g,[]);i=-71;return[[max(v*({*(f*20)[(i:=i+1)+j:][:2]}=={v})for v in f)for j in R]for R in b"9988 9``8 S``R SSRR".split()]
##
# -13 -14 13 12
def p(g):f=sum(g,[]);k=f*2;return[[max(v*({*k[i+j-70:][:2]}=={v})for i,v in enumerate(f))for j in R]for R in b"9988 9``8 S``R SSRR".split()]

### joking (144 bytes)
def p(g):f=sum(g,[]);k=f*99;i=0;return[[max(v*(k[(i:=i+1)-j%5]==k[i+12-j%3*13]==v)for v in f)for j in R]for R in b"KKHH KEEH AEEM AAMM".split()]

### ovs (148 bytes)
def p(g):f=sum(g,[]);k=f*2;return[[max(v*(k[i+1-j%5]*k[i+13-j%3*13]==v*v)for i,v in enumerate(f))for j in R]for R in b"KKHH KEEH AEEM AAMM".split()]

### combined (148 bytes)
def p(g):f=sum(g,[]);k=f*2;return[[max(v*(k[i+1-j%5]*k[i+13-j%3*13]==v*v)for i,v in enumerate(f))for j in R]for R in b"KKHH KEEH AEEM AAMM".split()]
