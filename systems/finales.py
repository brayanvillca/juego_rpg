from ui.pantalla import mostrar_escena

def final_fabiana(pantalla,jugador,texto):

    mostrar_escena(pantalla,texto)
    jugador.agregar_rasgo("Amor Verdadero")


def final_matias(pantalla,jugador):

    mostrar_escena(
        pantalla,
        "Matias derrota al dragon sacrificando su espada."
    )

    jugador.agregar_rasgo("Hermandad de Acero")

def final_secreto(pantalla, jugador):
    texto_secreto = """
    X. EL DESCUBRIMIENTO DE LA URNA

    Al llegar con el corazón puro y la protección de los bosques,
    la Urna Sagrada se manifiesta ante ti y Fabiana.

    No solo derrotaste al dragón, has roto la maldición eterna.

    Has obtenido el rasgo:
    SALVADOR DEL REINO
    """
    mostrar_escena(pantalla, texto_secreto)
    jugador.agregar_rasgo("Salvador del Reino")