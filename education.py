from abc import ABC,abstractmethod

class education(ABC):

    @abstractmethod
    def duration_course(education):
        pass
    def type_course(education):
        return 'Compulsary'


class technical(education):

    def duration_course(education):
        return '5'
    def type_course(education):
        return 'Engineering'


class nontechnical(education):

    def duration_course(education):
        return '3+2'

    def type_course(education):
        return 'Up to 14 years i.e.Childrens are mandatory'


v1 = technical()
v2 = nontechnical()


print(v1.duration_course())
print(v1.type_course())

print(v2.duration_course())
print(v2.type_course())