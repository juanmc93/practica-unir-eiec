# Práctica UNIR EIEC — Caso base

Pequeño proyecto para practicar **GitHub Flow** y **Pull Requests**.

## Estructura
- `sort_words.py`: script que ordena palabras desde un fichero o stdin.
- `palabras.txt`: fichero de ejemplo (una palabra por línea).
- `Makefile`: incluye la directiva `run-local` para ejecutar el script.

## Requisitos
- Python 3.8+
- (Opcional) Make

## Uso rápido
```bash
make run-local
# o
python3 sort_words.py palabras.txt --orden desc --unique
```

## Ejemplos
```bash
python3 sort_words.py palabras.txt --orden asc
python3 sort_words.py palabras.txt --orden desc --unique
echo -e "uva\npera\nmanzana" | python3 sort_words.py --orden asc
```
