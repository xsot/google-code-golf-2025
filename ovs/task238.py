def p(i):l,m=[[[a[0]for a in zip(b,*i)if{*a}&m]for b in i if{*b}&m]for m in[{8},{*range(1,8),9}]];return[[a<len(m)-1>b>0and(l[a-1][b-1]and m[1-(len(m)-1-b>a<b)|-(len(m)-1-b<a>b)][1-(len(m)-1-b>a>b)|-(len(m)-1-b<a<b)]or l[a-1][b-1])or m[a][b]for b in range(len(m))]for a in range(len(m))]
#
