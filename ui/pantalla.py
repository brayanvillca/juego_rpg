import pygame
import sys

pygame.font.init()
FUENTE = pygame.font.Font(None, 30)
FUENTE_GRANDE = pygame.font.Font(None, 36)
# ui/pantalla.py
COLOR_TEXTO = (240, 240, 240) # Blanco hueso, mejor para los ojos
COLOR_HIGHLIGHT = (0, 0, 0) # Turquesa real para títulos

def dibujar_texto(pantalla, texto, x, y, color=COLOR_HIGHLIGHT, fuente=None):
    fuente = FUENTE
    lineas = texto.split("\n")
    for i, linea in enumerate(lineas):
        img = fuente.render(linea, True, color)
        pantalla.blit(img, (x, y + i * 25))

def mostrar_escena(pantalla, texto, fondo=None):
    pantalla.fill((10, 10, 30))
    if fondo:
        fondo = pygame.transform.scale(fondo, (800, 600))
        pantalla.blit(fondo, (0, 0))

    dibujar_texto(pantalla, texto, 40, 5)
    dibujar_texto(pantalla, "Pulsa cualquier tecla para continuar", 40, 560)

    pygame.display.flip()
    esperando = True
    while esperando:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if e.type == pygame.KEYDOWN:
                esperando = False


def menu_opciones(pantalla, texto, opciones):
    while True:
        pantalla.fill((10, 10, 30))
        dibujar_texto(pantalla, texto, 40, 100)
        dibujar_texto(pantalla, f"Opciones validas: {', '.join(map(str, opciones))}", 40, 500)
        pygame.display.flip()
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_1 and 1 in opciones:
                    return 1
                if e.key == pygame.K_2 and 2 in opciones:
                    return 2
                if e.key == pygame.K_3 and 3 in opciones:
                    return 3