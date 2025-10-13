# i blacked out and this was here when i woke up
p=lambda i,s=[],k=3:-k*i or p([*zip(*i+s)],i[::-1],k-1)