from abc import abstractmethod,ABC


class mobile(ABC):

    @abstractmethod
    def memory_expandable(self):
        return

    def display(self):
        return 'Capacitive'

class samsung(mobile):

    def memory_expandable(samsung):
        return 'Memory_Expandable Up to 128 GB'
    def display(samsung):
        return'Almond Display'

class apple(mobile):

    def memory_expandable(apple):
        return 'Memory_Expandable Up to 256 GB'

    #def display( apple):
        #pass

        #return'Capacitive Display'


m1 = samsung()
m2 = apple()

print(m1.memory_expandable())
print(m1.display())

print(m2.memory_expandable())
print(m2.display())
