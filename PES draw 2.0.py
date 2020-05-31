import random
import datetime

x = ['MAN CITY','JUVENTUS','REAL MADRID','LIVERPOOL','BAYERN','PSG']
random.shuffle(x)

while x:
    Womble1 = x.pop()
    Wombat1 = x.pop()
    Womble2 = x.pop()
    Wombat2 = x.pop()

print((Womble1) + ' vs ' + (Wombat1) + 'WOMBAT HOME')
print((Womble2) + ' vs ' + (Wombat2) + 'WOMBLE HOME')

today = (datetime.datetime.strftime(datetime.datetime.today() , '%d/%m/%Y-  %Hh:%Mm'))
print (('this draw was held at ') + (today))
