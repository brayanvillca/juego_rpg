import pygame
import sys
pygame.font.init()
pygame.mixer.init()
COLOR_TURQUESA = (64, 224, 208)


def combate(pantalla, jugador, enemigo, sprites):
    vida_enemigo = enemigo.vida
    #SONIDOS
    sonido_golpe = pygame.mixer.Sound("assets/sonidos/golpe.wav")
    sonido_victoria = pygame.mixer.Sound("assets/sonidos/victoria.wav")
    sonido_derrota = pygame.mixer.Sound("assets/sonidos/derrota.wav")

    sonido_golpe.set_volume(0.5)
    
    atacando = False
    dragon_atacando = False
    delay = 0
    dragon_delay = 0
    reloj = pygame.time.Clock()
    fuente = pygame.font.Font(None, 34)
    fondo = pygame.transform.scale(sprites["lava"], (800, 600))

    prota_normal = pygame.transform.smoothscale(sprites["protagonista_normal"], (250, 250))
    prota_ataque = pygame.transform.smoothscale(sprites["protagonista_atacando"], (250, 250))
    dragon_normal = pygame.transform.smoothscale(sprites["dragon"], (280, 280))
    dragon_ataque = pygame.transform.smoothscale(sprites["dragon2"], (280, 280))

    while vida_enemigo > 0 and jugador.esta_vivo():
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if evento.type == pygame.KEYDOWN and evento.key == pygame.K_SPACE and not atacando:
                atacando = True
                vida_enemigo -= 1
                delay = 18
                sonido_golpe.play()  # 🔊 sonido ataque jugador

        pantalla.blit(fondo, (0, 0))
        sprite = prota_ataque if atacando else prota_normal
        sprite_dragon = dragon_ataque if dragon_atacando else dragon_normal
        pantalla.blit(sprite, (90, 280))
        pantalla.blit(sprite_dragon, (480, 250))

        texto_vida_jugador = fuente.render(f"Vida jugador: {jugador.vida}", True, COLOR_TURQUESA)
        texto_vida_enemigo = fuente.render(f"Vida dragon: {vida_enemigo}", True, COLOR_TURQUESA)
        texto_ayuda = fuente.render("Pulsa ESPACIO para atacar", True, COLOR_TURQUESA)
        pantalla.blit(texto_vida_jugador, (40, 30))
        pantalla.blit(texto_vida_enemigo, (40, 60))
        pantalla.blit(texto_ayuda, (40, 95))

        pygame.display.flip()

        if atacando:
            delay -= 1
            if delay <= 0:
                atacando = False
                if vida_enemigo > 0:
                    dragon_atacando = True
                    dragon_delay = 14
                
        if dragon_atacando:
            dragon_delay -= 1
            if dragon_delay <= 0:
                dragon_atacando = False
                sonido_golpe.play()
                
                # Lógica del Escudo Secreto
                if "Proteccion Elfica" in jugador.rasgos:
                    print("¡La protección absorbió el golpe!")
                    jugador.rasgos.remove("Proteccion Elfica") 
                else:
                    enemigo.atacar(jugador)

    if vida_enemigo <= 0:
        sonido_victoria.play()
        pygame.time.delay(1500)
    else:
        sonido_derrota.play()
        pygame.time.delay(1500)
    return jugador.esta_vivo() and vida_enemigo <= 0