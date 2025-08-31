# xsot (76 vs 70 bytes for gold)
import re
p=lambda m:eval(re.sub('(?<=5.{28}5..)5(?=..5.{28}5)','2',str(m)))
