# ovs (113 vs 2500 bytes for gold)
p=lambda i,e=enumerate:[[y*(sum(sum([z[b+b%~b:b+2]for z in i[a+a%~a:a+2]],[]))>y)for b,y in e(x)]for a,x in e(i)]

### combined (115 bytes)
p=lambda i,e=enumerate:[[y*(sum(sum([z[b-(b>0):b+2]for z in i[a-(a>0):a+2]],[]))>y)for b,y in e(x)]for a,x in e(i)]
