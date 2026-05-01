from game_flow import run_game


def main():
    try:
        run_game()
    except Exception as exc:
        import traceback

        print("\nSe produjo un error al ejecutar el juego:")
        print(exc)
        traceback.print_exc()
        input("\nPresiona ENTER para cerrar...")


if __name__ == "__main__":
    main()