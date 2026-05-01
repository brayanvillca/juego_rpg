class Jugador:

    def __init__(self, nombre):
        self.nombre = nombre
        self.vida = 3
        self.oro = 0
        self.rasgos = []

    def perder_vida(self, cantidad=1):
        self.vida = max(0, self.vida - cantidad)

    def ganar_oro(self, cantidad=2):
        self.oro += cantidad

    def agregar_rasgo(self, rasgo):
        if rasgo not in self.rasgos:
            self.rasgos.append(rasgo)

    def esta_vivo(self):
        return self.vida > 0