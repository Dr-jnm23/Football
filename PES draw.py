import random
import datetime

class Hat:
    def __init__(self):
        self.names = []
    def __repr__(self):
        return str(self.name)
    def insert_name(self, name):
        if name not in self.names:
            self.names.append(name)
        else:
            return
    def draw_name(self):
        drawname=random.choice(self.names)
        #changed here
        self.names.remove(drawname)
        return drawname

hat = Hat()
# insert teams in hat
# English

#European
#hat.insert_name('BARCA')
#hat.insert_name('BAYERN')
#hat.insert_name('JUVE')
#hat.insert_name('PSG')
#hat.insert_name('REAL MADRID')
#hat.insert_name('ATLETICO')
#hat.insert_name('INTER')

# World Cup doubles
hat.insert_name('BRAZIL')
hat.insert_name('ARGENTINA')
hat.insert_name('GERMANY')
hat.insert_name('ITALY')
hat.insert_name('PORTUGAL')
hat.insert_name('FRANCE')
hat.insert_name('ENGLAND')
hat.insert_name('BELGIUM')

print('Good evening and welcome to PES draw')
print('Wombles team first, then Wombats')
print((hat.draw_name()) + ' vs ' + (hat.draw_name()))
print('________________________________________________')
print((hat.draw_name()) + ' vs ' + (hat.draw_name()))
print('________________________________________________')
print((hat.draw_name()) + ' vs ' + (hat.draw_name()))
print('________________________________________________')
print((hat.draw_name()) + ' vs ' + (hat.draw_name()))
print('________________________________________________')

def currentTime():
    print("Current date and time : ")
today = (datetime.datetime.strftime(datetime.datetime.today() , '%d/%m/%Y-  %Hh:%Mm'))
print (('this draw was held at ') + (today))