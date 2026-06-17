import ast
import os
from pathlib import Path

# Caminho onde os arquivos das salas serão armazenados
caminhoArquivos = os.path.join(os.getcwd(), ".", "database")


def salvarSala(assentosSala: list, idSala: int):
    """
    Salva a lista de assentos de uma sala em um arquivo.

    Parâmetros:
        assentosSala (list): Lista composta contendo os assentos da sala.
        idSala (int): Identificador da sala.
    """

    # Monta o nome do arquivo com base no ID da sala
    nomeArquivo = Path(caminhoArquivos) / f"sala-{idSala}.txt"

    # Abre o arquivo para escrita (sobrescreve se já existir)
    with open(nomeArquivo, "w", encoding="utf-8") as arquivo:
        # Converte a lista para string e grava no arquivo
        arquivo.write(str(assentosSala))


def buscaSala(idSala: int):
    """
    Busca os assentos de uma sala a partir do arquivo.

    Parâmetros:
        idSala (int): Identificador da sala.

    Retorno:
        list: Lista de assentos da sala.
              Retorna lista vazia caso o arquivo não exista.
    """

    # Monta o nome do arquivo com base no ID da sala
    nomeArquivo = Path(caminhoArquivos) / f"sala-{idSala}.txt"

    # Cria um objeto Path para verificar a existência do arquivo
    arquivo = Path(nomeArquivo)

    # Se o arquivo não existir, retorna uma lista vazia
    if not arquivo.exists():
        return []

    # Abre o arquivo para leitura
    with open(nomeArquivo, "r", encoding="utf-8") as arquivo:
        # Converte o conteúdo textual de volta para uma lista Python
        return ast.literal_eval(arquivo.read())