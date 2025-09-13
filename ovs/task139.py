p=lambda i,v=11:-v*i or[[q+(v&(v:=v*2+q%3)>>9&1>>q)*7for q in r]for r in zip(*p(i,v-1)[::-1])]
