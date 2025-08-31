# combined (115 vs 108 bytes for gold)
p=lambda i,e=enumerate:[[y*(sum(sum([z[b-(b>0):b+2]for z in i[a-(a>0):a+2]],[]))>y)for b,y in e(x)]for a,x in e(i)]
