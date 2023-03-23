from Animal import Animal

class Cachorro(Animal):
    def fazer_barulho(self):
        print('Au au au!')
    

cachorro_nina = Cachorro('Nina',9.50)
cachorro_nina.fazer_barulho()