import re
p=lambda g,*G:eval(re.sub("([^2(]{9}2[^2]{9})",r"*[\1][::~0]","%s"%[*zip(*G or p(g,*g))]))