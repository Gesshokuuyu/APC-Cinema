# Cada filme possui:
# [nome, duracao_minutos, id_sala, quantidade_fileiras, assentos_por_fileira]
#  [0]        [1]           [2]            [3]                  [4]

from Src.fileHelper import salvarSala
from Src.cinema import (_visual_sala)
from Src.interfaceHelpers import limpaTerminal

filmes = [
    ["O Lobo de Wall Street", 180, 1, 5, 10],
    ["Todo Mundo em Pânico 6", 95, 2, 5, 15],
    ["Crepúsculo", 122, 3, 5, 10],
    ["Velozes e Furiosos 2", 107, 4, 5, 15],
    ["Piratas do Caribe 2", 151, 5, 5, 10]
]

filmesForaCartaz = [
    2
]

for filme_out in filmesForaCartaz:
    filmes.pop(filme_out)

print("=" * 40)
print("🎬 BEM-VINDO AO CINEMA 🎬")
print("=" * 40)

escolherFilmes = "S"

while escolherFilmes == "S":
        
    print("\nFilmes em cartaz:\n")

    for indice, filme in enumerate(filmes):
        print(f"[{indice}] {filme[0]}")
        print(f"    ⏱ Duração: {filme[1]} minutos")
        print("-" * 40)

    # Seleção do filme
    while True:
        try:
            escolha = int(input("\nSelecione o número do filme: "))

            if 0 <= escolha < len(filmes):
                break

            print("Filme inválido. Tente novamente.")

        except ValueError:
            print("Digite apenas números.")

    filme_selecionado = filmes[escolha]

    sala = _visual_sala(filme_selecionado)

    salvar = input("Deseja salvar os assentos reservados? [S/N]")

    if(salvar.upper() == 'S'):
        salvarSala(sala, filme_selecionado[2])
        limpaTerminal()
        print("Assentos salvos!")

    escolherFilmes = input("Deseja escolher outro filme? [S/N]")
