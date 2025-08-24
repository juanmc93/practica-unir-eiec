#!/usr/bin/env python3
import argparse, sys

def sort_list(words, descending=False, unique=False):
    items = words
    if unique:
        # elimina duplicados preservando el orden de aparición
        items = list(dict.fromkeys(items))
    return sorted(items, reverse=descending)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Sort words from a file or stdin.")
    parser.add_argument("file", nargs="?", help="Input file with one word per line. If omitted, reads stdin.")
    parser.add_argument("--orden", choices=["asc","desc"], default="asc", help="Orden de salida")
    parser.add_argument("--unique", action="store_true", help="Eliminar duplicados antes de ordenar")
    args = parser.parse_args()

    data = []
    if args.file:
        with open(args.file, encoding="utf-8") as f:
            data = [line.strip() for line in f if line.strip()]
    else:
        data = [line.strip() for line in sys.stdin if line.strip()]

    descending = (args.orden == "desc")
    for w in sort_list(data, descending=descending, unique=args.unique):
        print(w)
