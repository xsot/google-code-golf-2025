# ovs (60 bytes, gold)
p=lambda g:[(f:=sum(g,g))[f.index(5)+d:][:3]for d in b'	']

### combined (61 bytes)
p=lambda g:[(f:=sum(g,[]))[f.index(5)+d:][:3]for d in b'	']
