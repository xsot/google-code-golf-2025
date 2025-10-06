# ovs (121 bytes, gold)
p=lambda i:max(t:=[q for a in range(144)if any(min((h:=[*zip(*i[a%12:][:3])][a//12:][:3])+(q:=[*zip(*h)])))],key=t.count)

### combined (123 bytes)
p=lambda i:max(t:=[h for a in range(144)if all(map(any,(h:=[x[a//12:][:3]for x in i[a%12:][:3]])+[*zip(*h)]))],key=t.count)
