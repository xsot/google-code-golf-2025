p=lambda m:[*map(list,zip(sorted({*(a:=sum(m,[]))},key=a.count)))][2::-1]
# same as task393 (f8ff0b80)