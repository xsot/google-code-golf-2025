def p(p):
 a=sum(p,e:=[]);p=[];n=[[]];r=15
 for i in range(16):
  if(5in a[i::r])>i/r:p+=[i]
  elif p:i=[n for n in range(150)if a[n]>4and n%r in p];e+=[[n-i[0]for n in i]];p=[];n=[i+[n]for i in n for n in range(45)if 1>a[n]]
 for i in n:
  i=[any(n-i in e*(6>i%r-n%r)for i,e in zip(i,e))|a[n]%5for n in range(150)]
  if all(i[:45])*(i.count(0)==a.count(0)):return[i[n*r:][:r]for n in range(10)]