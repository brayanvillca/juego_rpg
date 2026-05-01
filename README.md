# 🗡️ Aventura RPG: El Misterio de la Urna

Un videojuego de rol narrativo y combate por turnos desarrollado en **Python** con la librería **Pygame**. El jugador debe tomar decisiones críticas, gestionar su salud y enfrentarse a un poderoso dragón para salvar el reino.

---

## 📸 Capturas de Pantalla

| Inicio del Viaje | Encuentro con Mei | Combate Final |
| :---: | :---: | :---: |
| ![Inicio](https://via.placeholder.com/300x200?text=Pueblo+Inicio) | ![Mei](https://via.placeholder.com/300x200?text=Diálogo+con+Mei) | ![Combate](https://via.placeholder.com/300x200?text=Lucha+vs+Dragón) |
| *Exploración inicial* | *Decisiones narrativas* | *Acción por turnos* |

---

## 🌟 Características Principales

- **Sistema Narrativo Modular:** Los diálogos y eventos se cargan dinámicamente desde archivos independientes.
- **Mecánicas de Combate:** Sistema de turnos con animaciones de ataque, sonidos (`.wav`) y gestión de vida.
- **Eventos Aleatorios:** Cruce de caminos donde puedes ganar oro o perder salud.
- **🔓 El Final Secreto:** Solo los jugadores más hábiles pueden desbloquear el final "Salvador del Reino" si cumplen tres requisitos:
  1. Elegir a **Fabiana** como compañera.
  2. Obtener la **Protección Élfica** (decisión moral).
  3. Finalizar el combate con el **100% de vida (3/3)**.

---

## 🛠️ Tecnologías

- **Lenguaje:** Python 3.8+
- **Librería:** [Pygame](https://www.pygame.org/)
- **Paradigma:** Programación Orientada a Objetos (POO) y Modular.

---

## 📂 Estructura del Proyecto

```text
├── main.py                 # Punto de entrada del juego
├── game_flow.py            # Orquestador de la lógica principal
├── core/                   # Clases base (Jugador, Enemigo)
├── systems/                # Motores de combate, eventos y finales
├── story/                  # Archivos de texto narrativo
├── ui/                     # Lógica de renderizado y menús
└── assets/                 # Recursos gráficos y de audio