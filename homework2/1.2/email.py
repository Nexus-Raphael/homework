# #就我目前所掌握的,只能查找出某些常用的邮箱地址,见谅.

import re
r=r'(^[\w-]+(\.[\w-]+)*@(qq|outlook|163|126|gmail|sina|hotmail|139|sohu|icloud|smail)(\.[\w-]+)+$)'
adress='alphal.it.is.my.turn@outlook.com'
print(re.match(r,adress))
