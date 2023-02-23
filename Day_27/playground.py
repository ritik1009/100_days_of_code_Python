def add(*args):
    total = 0
    for i in args:
        total+=i
    print(total)

#add(1,2,3,7)

class Car:
    def __init__(self,**kw):
        self.make = kw.get('make')
        self.model = kw.get('model')

car1 = Car(make = 'Nissan',model = 'gtr')