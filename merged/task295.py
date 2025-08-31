# att (54 bytes, gold)
p=lambda a:[b:=a[0]]+[b:=b[:1]+b[:-1]for _ in b[2::2]]

### xsot (59 bytes)
p=lambda m:eval("m"+~-len(r:=m[0])//2*"+[r:=r[:1]+r[:-1]]")
##
p=lambda m:eval("m"+~-len(r:=m[0])//2*"+[r:=r[:1]+r[:-1]]")
p=lambda m:m+[*eval(~-len(r:=m[0])//2*"(r:=r[:1]+r[:-1]),")]
p=lambda m:(r:=m[0],*eval(~-len(r)//2*"(r:=r[:1]+r[:-1]),"))
p=lambda m:[r:=m[0]]+[r:=r[:1]+r[:-1]for _ in~-len(r)//2*m]
p=lambda m:(l:=len(r:=m[0]))and[[r[0]]*i+r[:l-i]for i in range(l//2)]
p=lambda m:[[m[0][0]]*i+m[0][:len(m[0])-i]for i in range(len(m[0])//2)]
