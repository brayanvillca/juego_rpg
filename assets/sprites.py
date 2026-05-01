import os
import pygame

EXTENSIONES_COMPATIBLES = (".png", ".jpg", ".jpeg", ".bmp")


def _ruta_imagenes():
    """Return absolute path to project's images directory."""
    return os.path.join(os.path.dirname(__file__), "images")


def _resolver_ruta(nombre_archivo):
    base, ext = os.path.splitext(nombre_archivo)
    candidatos = [nombre_archivo] if ext else []
    candidatos.extend(f"{base}{extension}" for extension in EXTENSIONES_COMPATIBLES)

    for candidato in candidatos:
        ruta = os.path.join(_ruta_imagenes(), candidato)
        if os.path.exists(ruta):
            return ruta
    return None


def _cargar_imagen(nombre_archivo, alpha=True, size=(800, 600)):

    ruta = _resolver_ruta(nombre_archivo)
    if ruta:
        try:
            imagen = pygame.image.load(ruta)
            return imagen.convert_alpha() if alpha else imagen.convert()
        except pygame.error:
            # Algunos builds de pygame (segun SO/Python) no incluyen soporte JPEG.
            pass

    fallback = pygame.Surface(size, pygame.SRCALPHA if alpha else 0)
    fallback.fill((60, 60, 80))
    return fallback


def cargar_sprites():
    sprites = {
        # protagonista
        "protagonista_normal": _cargar_imagen("prota", alpha=True, size=(180, 180)),
        "protagonista_atacando": _cargar_imagen("prota_pose_ataque", alpha=True, size=(180, 180)),

        # dragon
        "dragon": _cargar_imagen("dragon_pose_normal", alpha=True, size=(220, 220)),
        "dragon2": _cargar_imagen("dragon_pose_ataque", alpha=True, size=(220, 220)),
        "cueva_dragon": _cargar_imagen("fondo_cueva_dragon", alpha=True, size=(220, 220)),

        # fondos
        "capital": _cargar_imagen("fondo_villa", alpha=False),
        "bosque": _cargar_imagen("fondo_bosque", alpha=False),
        "mazmorra": _cargar_imagen("fondo_calabozo", alpha=False),
        "ruinas": _cargar_imagen("fondo_ruinas", alpha=False),
        "pueblo": _cargar_imagen("fondo_aldea", alpha=False),
        "lava": _cargar_imagen("fondo_cueva_dragon", alpha=False),
        "templo": _cargar_imagen("fondo_santuario", alpha=False),
        "montana": _cargar_imagen("fondo_camino", alpha=False),

    }

    return sprites
