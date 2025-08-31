# joking+mwi (61 vs 60 bytes for gold)
p=lambda g:[(f:=sum(g,[]))[f.index(5)+d:][:3]for d in b'	']

### ovs (tied, 61 bytes)
p=lambda g:[(f:=sum(g,[]))[f.index(5)+d:][:3]for d in b'	']
