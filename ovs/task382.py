p=lambda i,k=-7:k*i or p([*zip(w:=i.pop(0),*[i,[[f]+(w:=[0,*w][f<1:])[1:]for f,*_ in i]][max(i)[0]and'8'not in'%s'%i])][::k%4<1or-1],k+1)
