import ast
import os
from pathlib import Path

caminhoArquivos = os.path.join(os.getcwd(), ".", "database")

def salvarSala(assentosSala: list, idSala: int):

    nomeArquivo = Path(caminhoArquivos) / f"sala-{idSala}.txt"

    with open(nomeArquivo, "w", encoding="utf-8") as arquivo:
        arquivo.write(str(assentosSala))

def buscaSala(idSala: int):

    nomeArquivo = Path(caminhoArquivos) / f"sala-{idSala}.txt"

    arquivo = Path(nomeArquivo)

    if not arquivo.exists():
        return []
    
    with open(nomeArquivo, "r", encoding="utf-8") as arquivo:
        return ast.literal_eval(arquivo.read())
