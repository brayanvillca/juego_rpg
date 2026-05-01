def aplicar_evento(evento, jugador):
    if "+2 de oro" in evento:
        jugador.ganar_oro(2)
        print("¡Ganaste oro!") 
        
    if "-1 de vida" in evento:
        jugador.perder_vida(1)
        print("¡Perdiste vida!")

    if "+1 de vida" in evento:
        if jugador.vida < 3:
            jugador.vida += 1 
            print("¡Recuperaste salud!")