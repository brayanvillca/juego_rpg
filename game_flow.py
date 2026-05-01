import random

import pygame

from assets.sprites import cargar_sprites
from core.enemigo import Enemigo
from core.jugador import Jugador
from story.texto_capital import TEXTO_CAPITAL
from story.texto_dragon import TEXTO_DRAGON
from story.texto_eventos import EVENTOS
from story.texto_finales import TEXTO_DECISION_FINAL, TEXTO_NUEVA_PARTIDA
from story.texto_inicio import TEXTO_INICIO
from story.texto_mei import TEXTO_MEI
from story.texto_personajes import TEXTO_COMPANERO, TEXTO_FABIANA, TEXTO_MATIAS
from systems.combate import combate
from systems.eventos import aplicar_evento
from ui.pantalla import menu_opciones, mostrar_escena
from systems.finales import final_fabiana, final_matias, final_secreto

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
GAME_TITLE = "Aventura RPG"


def _mostrar_resumen_final(pantalla, jugador):
    rasgos = ", ".join(jugador.rasgos) if jugador.rasgos else "Ninguno"
    mostrar_escena(
        pantalla,
        f"""{TEXTO_NUEVA_PARTIDA}

ORO: {jugador.oro}
VIDA: {jugador.vida}
RASGOS: {rasgos}
""",
    )


def run_game():
    pygame.init()
    pantalla = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption(GAME_TITLE)

    try:
        sprites = cargar_sprites()
        jugador = Jugador("Aventurero")

        mostrar_escena(pantalla, TEXTO_INICIO,sprites["pueblo"])
        mostrar_escena(pantalla, TEXTO_CAPITAL, sprites["capital"])
        mostrar_escena(pantalla, TEXTO_FABIANA, sprites["capital"])
        mostrar_escena(pantalla, TEXTO_MATIAS, sprites["capital"])

        opcion = menu_opciones(pantalla, TEXTO_COMPANERO, [1, 2])
        companero = "Matias" if opcion == 1 else "Fabiana"

        evento = random.choice(EVENTOS)
        mostrar_escena(pantalla, evento)
        aplicar_evento(evento, jugador)

        if not jugador.esta_vivo():
            mostrar_escena(pantalla, "Las heridas del camino fueron demasiado graves.")
            _mostrar_resumen_final(pantalla, jugador)
            return

        respuesta = menu_opciones(pantalla, TEXTO_MEI, [1, 2, 3])
        if respuesta in [2, 3]:
            jugador.agregar_rasgo("Proteccion Elfica")
            mostrar_escena(pantalla, "Mei te concede proteccion elfica.")

        mostrar_escena(pantalla, TEXTO_DRAGON, sprites["lava"])
        dragon = Enemigo("Dragon Corrompido", 3, 1)
        victoria = combate(pantalla, jugador, dragon, sprites)
        
        if victoria:
            # Verificamos requisitos del final secreto
            tiene_proteccion = "Proteccion Elfica" in jugador.rasgos
            es_perfecto = jugador.vida == 3
            
            if companero == "Fabiana" and tiene_proteccion and es_perfecto:
                final_secreto(pantalla, jugador)
            elif companero == "Fabiana":
                final_fabiana(pantalla, jugador, TEXTO_DECISION_FINAL)
            else:
                final_matias(pantalla, jugador)
        else:
            mostrar_escena(pantalla, "El dragon te ha derrotado. El reino cae en sombras.")

        _mostrar_resumen_final(pantalla, jugador)
    finally:
        pygame.quit()
