# att (105 bytes, gold)
p=eval(f"lambda a:max(b:=[a {'for*a,in map(zip,a,a[1:],a[2:])'*2}if any(min(*a,*zip(*a)))],key=b.count)")

### ovs (121 bytes)
p=lambda i:max(t:=[q for a in range(144)if any(min((h:=[*zip(*i[a%12:][:3])][a//12:][:3])+(q:=[*zip(*h)])))],key=t.count)

### combined (123 bytes)
p=lambda i:max(t:=[h for a in range(144)if all(map(any,(h:=[x[a//12:][:3]for x in i[a%12:][:3]])+[*zip(*h)]))],key=t.count)
