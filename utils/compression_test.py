from compression import compress
import warnings
import re
import time
warnings.filterwarnings("ignore")

ma = 999
coun = 0
perc = 1
tim = time.time()
sizes = []

substitutions = [
  (" ", "\t"),
  #("'", '"'),
  #('"', "'"),
]

import itertools
def perms(expression, splitter : str):
   return map(splitter.join, itertools.permutations(expression.split(splitter) if type(expression) is str else expression))

def zip_replace(src,prev_vals = [], mult = 1):
 if "#" in src:
  z = re.search(r"#(\[[^#]+\])##", src)
  e = eval(z[1])
  for t in e:
   zip_replace(re.sub(r"#\[[^#]+\]##", str(t), src, 1), prev_vals + [t], mult*len(e))
 else:
    zipped_src, _ = compress(src.encode(),rand_passes=100,pre_and_post=False)

    for sub in substitutions:
        s = src.replace(*sub)
        z2, _ = compress(s.encode(),rand_passes=100,pre_and_post=False)
        if len(z2) < len(zipped_src):
           src = s
           zipped_src = z2

    global coun,perc,tim,ma,sizes
    coun += 1
    if coun > mult*perc//100:
        perc=coun*100//mult+1
        print("%d/%d"%(coun,mult))
        print('est', int((time.time()-tim)*((mult-coun)/coun)), 'sec remaining')
    l = len(zipped_src)
    sizes += [{'length': l, 'vals': prev_vals}]
    if l < ma:
        print(ma := l)
        print(src)

code = open("compression_test.txt").read()
zip_replace(code)
print('best', ma)
print('aver', sum(s['length'] for s in sizes)/len(sizes))

vals = [s['vals'] for s in sizes]
for n in range(len(vals[0])):
    s = {s[n] for s in vals}
    if len(s) > 1:
        print("branch",n)
        for v in s:
            t = [s['length'] for s in sizes if s['vals'][n] == v]
            print('aver', "%.02f"%(sum(t)/len(t)), repr(v))