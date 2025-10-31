S='+[*map(any,g:=[*zip(*g)])].index(1)'*2
p=eval(f"lambda g:[g:=[[g[J][I]|((g*2)[I-{S}]*2)[4{S}-J]{'for %s in range(10)]'*3%(*'IJ_',)}[3]")