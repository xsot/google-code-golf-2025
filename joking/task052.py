p=lambda a:[3*[(b==b[:1]*3)*5]for b in a]

##
p=lambda a:[3*[1//len({*b})*5]for b in a]
p=lambda a:[3*[[*{*b},0,0,5][3]]for b in a]
p=lambda a:[3*[({*b}=={b[0]})*5]for b in a]
p=lambda a:[3*[(b[0]==b[1]==b[2])*5]for b in a]
p=lambda a:[3*[(b[:2]==b[1:])*5]for b in a]
p=lambda a:[3*[(b==[*{*b}]*3)*5]for b in a]
p=lambda a:[3*[min(b)//max(b)*5]for b in a]