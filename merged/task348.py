# att (101 bytes, gold)
p=lambda a,n=-13:n*a or p([[c|-d%15for c,d in zip(a.pop(0),[0]+b)][::-1]for*b,_ in a[1:]+a[-1:]],n+1)

### combined (tied, 101 bytes)
p=lambda a,n=-13:n*a or p([[c|-d%15for c,d in zip(a.pop(0),[0]+b)][::-1]for*b,_ in a[1:]+a[-1:]],n+1)
