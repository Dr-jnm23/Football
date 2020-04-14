import random
import datetime

x = ['GER','BRA','ENG','ARG','BEL','ITA','FRA','POR']
random.shuffle(x)

while x:
    Womble1 = x.pop()
    Wombat1 = x.pop()
    Womble2 = x.pop()
    Wombat2 = x.pop()
    Womble3 = x.pop()
    Wombat3 = x.pop()
    Womble4 = x.pop()
    Wombat4 = x.pop()

print((Womble1) + ' vs ' + (Wombat1))
print((Womble2) + ' vs ' + (Wombat2))
print((Womble3) + ' vs ' + (Wombat3))
print((Womble4) + ' vs ' + (Wombat4))

today = (datetime.datetime.strftime(datetime.datetime.today() , '%d/%m/%Y-  %Hh:%Mm'))
print (('this draw was held at ') + (today))