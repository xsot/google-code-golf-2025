def p(a):I=[a+a for a in a+a];return[[[I[x][y]|I[a-b+y][a+b+n+~x]|I[a+a+n+~x][b+b+n+~y]|I[a+b+n+~y][b-a+x]for y in range(10)]for x in range(10)]for n in range(10)for b in range(10)for a in range(10)if all(all(a[b:b+n])for a in I[a:a+n])][-1]

##
def p(a):I=[a+a for a in a+a];return[[[#[*perms('I[x][y]|I[a-b+y][a+b+n+~x]|I[a+b+n+~y][b-a+x]|I[a+a+n+~x][b+b+n+~y]','|')]##for y in range(10)]for x in range(10)]for n in range(10)for #[*'ab']## in range(10)for #[*{'a','b'}-{prev_vals[-1]}]## in range(10)if all(all(#[*'axy']##[b:b+n])for #[prev_vals[-1]]## in I[a:a+n])][-1]

## unzipped short, 200 bytes
exec("def p(a):I=[a*2for a in a*2];return[[[I[x][y]|I[a+b+n+~y][b-a+x]|I[a-b+y][a+b+n+~x]|I[a+a+n+~x][b+b+n+~y]"+'for %s in range(10)%s'*5%(*'y]x]n a b','if all(all(x[b:b+n])for x in I[a:a+n])][-1]'))