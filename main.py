# Cada filme possui:
# [nome, duracao_minutos, id_sala, quantidade_fileiras, assentos_por_fileira]
#  [0]        [1]           [2]            [3]                  [4]


from Src.cinema import (_visual_sala)

filmes = [
    ["O Lobo de Wall Street", 180, 1, 5, 10],
    ["Todo Mundo em Pânico 6", 95, 2, 5, 15],
    ["Crepúsculo", 122, 3, 5, 10],
    ["Velozes e Furiosos 2", 107, 4, 5, 15],
    ["Piratas do Caribe 2", 151, 5, 5, 10]
]

print("=" * 40)
print("🎬 BEM-VINDO AO CINEMA 🎬")
print("=" * 40)

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

print("Deseja salvar a sala cadastrada?")
