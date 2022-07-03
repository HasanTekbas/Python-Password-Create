import random

lower="abcdefghijklmnoprstuvyz"
upper="ABCDEFGHIJKMLMNOPRSTUVYZ"
number="0123456789"
symbol="!@#$%"      
all = lower + upper + number + symbol;
length = 12
password = "".join(random.salmpe(all,length))
print(password)  


