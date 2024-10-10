import math

print(math.fabs(-10))

target = [0,1,2,3,4,5]

print(all(target))
print(any(target))

c_num = 62

print(ascii(c_num))

c = 2

print(bin(c))
print(oct(c))
print(hex(c))

class Sample:
    def __init__(self, name):
        self.name = name
    
    @classmethod
    def class_method(self, name):
        print(name) 
    
    @staticmethod
    def static_method(self):
        print('static_method')

#?????
Sample.static_method()

Sample('name').class_method()