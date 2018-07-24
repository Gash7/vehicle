from abc import ABC,abstractmethod

class vehicle(ABC):
    @abstractmethod
    def engine_capacity(vehicle):
        pass

    def typeofvehicle(vehicle):
        return 'Sedan'

class Audi(vehicle):
    def engine_capacity (vehicle):
        return'2250'


    def typeofvehicle (vehicle):
        return'Sedan'

class BMW (vehicle):

    def engine_capacity (vehicle):
        return



v1 = Audi()
v2 = BMW()

#print(v1.__dict__)
print(v1.engine_capacity())
print(v1.typeofvehicle())
#print(v2.__dict__)
print(v2.engine_capacity())
print(v2.typeofvehicle())
