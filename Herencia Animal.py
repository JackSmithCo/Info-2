class ave:
    def __init__(self,tipo,vuela):
        self.ave=tipo
        self.vuelo=vuela
        self.oviparo=True
        self.pico=True

    def comer(self,comida):
        print("Este tipo de ave come normalmente: ",comida)
        






class gallina(ave):
    pass

p=ave("gallina",False)
p.volar()
p.comer("maiz")

g=ganso("carnivoro",True,"nadar","4")
g.destreza