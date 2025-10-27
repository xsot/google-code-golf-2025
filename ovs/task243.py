p=lambda a:exec("a[::-1]=zip(*eval(str(a).replace('1, 0','1,1')));"*80)or a
