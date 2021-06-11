# 백준 1918번 후위표기식
import re
s = '(A+(B*C))-(D/E)'
cal = re.findall('\\([A-Z*\\/\\-+]+\\)',s)
for c in cal:
    if 
