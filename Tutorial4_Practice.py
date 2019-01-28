class Student:

    name = 'avinav'

    def __init__(self,name):
        # name = 'kedar'
        print('using inst', name)    #inder

        # self.name = name  #avinav
        print('using self ',self.name)

        print('calling by class',Student.name) #avinav

s1 = Student('inder')

