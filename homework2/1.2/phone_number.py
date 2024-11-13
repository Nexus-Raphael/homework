import re

text=input()
pn=r'\d{3}-\d{8}'
print(re.findall(pn,text))
