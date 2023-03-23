from Bicho import Bicho

class Animal(Bicho):
    def __init__(self,peso,nome) :
        super().__init__(peso)   #  Super para satisfazer o minha condição do peso
        self.nome = nome         # Variável propria nome
       
    def fazer_barulho(self):
        print('Fez barulho genérico')