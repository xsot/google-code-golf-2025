# Garry modified from kenkridge's notebook https://www.kaggle.com/code/kenkrige/chipping-skills-3-regex/comments
import re
def p(i):
 r=re.sub(', ','',str(i+[*zip(*i)]));r+=r[::-1];i=int(max(r,key=r.count));l={0:(0,i)}
 for t in range(10):
  if(t!=i)*(e:=re.findall(f'{t}+',r)):d=len((re.findall(f'{t}{t}([^]){t}]+){t}',r)or[''])[0]);o=len(max(e))*((d>0)+1);l[o+d>>1]=d+1>>1,t
 return[[i*((d:=l[r[1]])[0]>r[0])or d[1]for t in range(-max(l),max(l)+1)if(r:=sorted((abs(t),abs(e))))]for e in range(-max(l),max(l)+1)]