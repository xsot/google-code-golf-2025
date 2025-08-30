# joking+mwi (123 bytes, gold)
p=lambda i:max(t:=[h for a in range(144)if all(map(any,(h:=[x[a//12:][:3]for x in i[a%12:][:3]])+[*zip(*h)]))],key=t.count)
