# zip fiddling
def p(i):f=sum(i,[]);w=sum(2<<J for J in range(50)if f[J]<5in{*i[J//10][:J%10]}&{*i[J//10][J%10:]});i=[[J^c*(1&(w:=w>>1)or J==c)for J in J]for c in{*f}if bin(sum(2<<J for J in range(100)if f[J]==c)<<9)in bin(w<<95)for J in i][::-1];f=sum(i,[]);w=sum(2<<J 
for J in range(50)if f[J]<5in{*i[J//10][:J%10]}&{*i[J//10][J%10:]});i=[[J^c*(1&(w:=w>>1)or J==c)for J in J]for c in{*f}if bin(sum(2<<J for J in range(100)if f[J]==c)<<9)in bin(w<<95)for J in i][::-1];return i


##
def p(i):#[
"f=sum(i,[]);w=sum(2<<J for J in range(50)if f[J]<5in#['{*i[J//10][:J%10]}&{*i[J//10][J%10:]}','{*f[J//10*10:J]}&{*f[J:J//10*10+10]}']##);i=[[J^c*(#[*perms('1&(w:=w>>1)','&'),'(w:=w>>1)%2']##or J==c)for J in J]for c in{*f}if bin(sum(2<<J for J in range(100)if f[J]==c)<<9)in bin(w<<#[*range(93,100)]##)for J in i][::-1];"
]###[prev_vals[-1]]##return i