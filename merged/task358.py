# att (105 vs 97 bytes for gold)
p=lambda a:[*map(f:=lambda*b:1<(n:=len({*b})-1)and[max(b[i%n::n])for i in range(len(b))]or b,*map(f,*a))]
