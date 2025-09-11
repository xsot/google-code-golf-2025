# subtract from each cell
# if all 4 adjacent cells are non-zero
# and the y coord isnt on the first or last row.
# to check which color, we set t to the index of the empty row separating the yellow rectangles
# and check whether there are more yellow squares above it or below it
p=lambda g,r=range(10):[[g[y][x]-all(g[y-z%11][x-z//11]for z in b"	c")*(y%9>0)*(2|((y>(t:=g[1:].index(min(g))+1))!=(sum(sum(g[t:],[]))>sum(sum(g[:t],[])))))for x in r]for y in r]