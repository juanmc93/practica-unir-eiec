import argparse

def main():
    parser = argparse.ArgumentParser(description="Ordena palabras desde un archivo")
    parser.add_argument("archivo", help="Ruta del archivo de texto con palabras")
    parser.add_argument("--orden", choices=["asc", "desc"], default="asc",
                        help="Orden de las palabras (asc o desc). Por defecto: asc")
    parser.add_argument("--unique", action="store_true",
                        help="Elimina palabras repetidas antes de ordenar")
    args = parser.parse_args()

    # Leer archivo
    with open(args.archivo, "r") as f:
        palabras = f.read().split()

    # Eliminar duplicados si se usa --unique
    if args.unique:
        palabras = list(set(palabras))

    # Ordenar
    palabras.sort(reverse=(args.orden == "desc"))

    # Imprimir resultado
    for palabra in palabras:
        print(palabra)

if __name__ == "__main__":
    main()
