import random

lower="abcdefghijklmnoprstuvyz"
upper="ABCDEFGHIJKMLMNOPRSTUVYZ"
number="0123456789"
symbol="!@#$%"      
all = lower + upper + number + symbol;
length = 12
password = "".join(random.salmpe(all,length))
print(password)  


#print(hash(password))
# konuyla alakali kullanici girsin mail + sifre kullanicinin animsayacagi bir sifre girecek.
# benim taradfimdan olusan sifre cozucu de yapacaksin
# microsft visio bu program ile akis cizergesi ve diyagram olusturmaya yarar akis diyagrami yapilacak