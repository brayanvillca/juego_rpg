class Enemigo:

    def __init__(self,nombre,vida,daño):

        self.nombre = nombre
        self.vida = vida
        self.daño = daño

    def atacar(self,jugador):

        jugador.perder_vida(self.daño)