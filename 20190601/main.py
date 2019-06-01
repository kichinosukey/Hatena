import sys

class Body:

    def __init__(self, style=None, door=None):
        self.style = style
        self.door = door
    
    def __str__(self):
        s = ''
        s += self.style + '\n'
        s += str(self.door) + '\n'
        return s

    def add(self, style=None, door=None):
        if style is not None:
            self.style = style
        if door is not None:
            self.door = door

class Car:

    def __init__(self, name, body=Body()):
        self.name = name
        self.body = body

    def __str__(self):
        s = ''
        s += self.name + '\n'
        s += self.body.__str__() + '\n'
        return s
        
    def add_param_to_body(self, style=None, door=None):
        if self.body is not None:
            self.body.add(style=style, door=door)

class Car_rev(Car):

    def __init__(self, name):
        self.name = name
        self.body = Body()

if __name__ == '__main__':

    args = sys.argv

    if args[1] == 'case1':

        A_car = Car('A')
        A_car.add_param_to_body('sedan', 4)
        B_car = Car('B')
        B_car.add_param_to_body('coupe', 2)

        print(A_car)
        print(B_car)
    
    elif args[1] == 'case2':
    
        A_car = Car_rev('A')
        A_car.add_param_to_body('sedan', 4)
        B_car = Car_rev('B')
        B_car.add_param_to_body('coupe', 2)

        print(A_car)
        print(B_car)
 
    elif args[1] == 'analyse1':

        A_car = Car('A')
        A_car.add_param_to_body('sedan', 4)
        B_car = Car('B')
        B_car.add_param_to_body('coupe', 2)

        print('A_car: %d' % id(A_car))
        print('A_car body: %d' % id(A_car.body))

        print('B_car: %d' % id(B_car))
        print('B_car body: %d' % id(B_car.body))

    elif args[1] == 'analyse2':

        A_car = Car_rev('A')
        A_car.add_param_to_body('sedan', 4)
        B_car = Car_rev('B')
        B_car.add_param_to_body('coupe', 2)

        print('A_car: %d' % id(A_car))
        print('A_car body: %d' % id(A_car.body))

        print('B_car: %d' % id(B_car))
        print('B_car body: %d' % id(B_car.body))