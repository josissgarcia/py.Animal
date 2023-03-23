from Animal import Animal

class Gato(Animal):
    def fazer_barulho(self):
        print('Miau miau!')
        

gato_Bob = Gato('Bob',6)
gato_Bob.fazer_barulho()



