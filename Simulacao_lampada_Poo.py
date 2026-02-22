class Lampada():
    def __init__(self):
        self.luz = False


    def ligar(self):
        self.luz = True
        print("Lampada foi ligada")

    def interruptor(self):
        if self.luz == True:
            self.luz = False
            print("A Lampada foi desligada")
        
        else:
            self.luz = True
            print("A  lampada foi ligada")
    
    def desligar(self):
        if self.luz == True:
            self.luz = False
            print("Lampada foi desligada")
        
        else:
            print("A lampada já está desligada")




p1 = Lampada()

p1.ligar()
p1.interruptor()
p1.interruptor()
p1.desligar()

