from Animal import Animal

class Ave(Animal):
    def __init__(self, tem_asas):
        super().__init__(14, "Bil")
        self.tem_asas =True
          
    def fazer_barulho(self):
        super().fazer_barulho()
        
        
        
ave_peru=Ave(True)

ave_peru.fazer_barulho()

ave_peru.outro_barrlho()