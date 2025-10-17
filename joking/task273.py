p=lambda g,R={*range(10)}:[[g[i][j]|len({g[I][J]*(i>I,j>J)for I in R^{i}for J in{j}^R})//5*2for j in R]for i in R]

##
exec("p=lambda g:[[g[i][j]|len({g[I][J]*(i>I,j>J)"+"for %s in{*range(10)}%s"*4%('I','-{i}','J','-{j}})//5*2',*'j]i]'))