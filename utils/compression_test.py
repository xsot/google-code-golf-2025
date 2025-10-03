from compression import compress
import warnings
import re
import time
warnings.filterwarnings("ignore")

ma = 999
coun = 0
perc = 1
tim = time.time()

def zip_replace(src,prev_vals = [], mult = 1):
 if "#" in src:
  z = re.search(r"#(\[[^#]+\])##", src)[1]
  e = eval(z)
  for t in e:
   zip_replace(re.sub(r"#\[[^#]+\]##", str(t), src, 1), prev_vals + [t], mult*len(e))
 else:
    zipped_src, _ = compress(src.encode())
    global coun,perc,tim,ma
    coun += 1
    if coun > mult*perc//100:
        perc=coun*100//mult+1
        print("%d/%d"%(coun,mult))
        print('est', int((time.time()-tim)*((mult-coun)/coun)), 'sec remaining')
    l = len(zipped_src)
    if l < ma:
        print(ma := l)
        print(src)

code = open("compression_test.txt").read()
zip_replace(code)