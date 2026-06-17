from Src.interfaceHelpers import limpaTerminal
from Src.fileHelper import buscaSala

def renderizarSalaInicial(idSala: int, fileiras: int, assentos: int):
    salaSalva = buscaSala(idSala)
    sala = []

    print("  ", end="")
    for assento in range(1, assentos + 1):
        print(f"{assento:^5}", end="")
    print()

    for fileira in range(1, fileiras + 1):
        print(f"{fileira:<3}", end="")

        for assento in range(1, assentos + 1):

            ocupado = False

            for lugar in salaSalva:
                if lugar[0] == fileira and lugar[1] == assento:
                    ocupado = lugar[2]
                    break

            if ocupado:
                print("[X]  ", end="")
                sala.append([fileira, assento, True])
            else:
                print("[ ]  ", end="")
                sala.append([fileira, assento, False])

        print()

    return sala, fileiras * assentos


# ====================================================================

def renderizaSala(sala: list, fileiras: int, assentos: int):
    print("  ", end="")
    for assento in range(1, assentos + 1):
        print(f"{assento:^5}", end="")
    print()

    for fileira in range(1, fileiras + 1):
        print(f"{fileira:<3}", end="")
        for lugar in sala:
            if lugar[0] == fileira:
                icone = "[X]" if lugar[2] else "[ ]"
                print(f"{icone:^5}", end="")
        print()

# ====================================================================


def _visual_sala(filmeEscolhido: list):
    idSala = filmeEscolhido[2]
    fileiras = filmeEscolhido[3]
    assentos = filmeEscolhido[4]

    sala, assentosDisponiveis = renderizarSalaInicial(idSala, fileiras, assentos)

    print("\n")
    print("=" * 77)
    cadastrando = True
    cadastros = 0

    while cadastros < assentosDisponiveis and cadastrando == True:
        limpaTerminal()
        print("FILME SELECIONADO:")
        titulo = filmeEscolhido[0]
        largura = len(titulo) + 4

        print("+" + "-" * largura + "+")
        print(f"|  {titulo.upper()}  |")
        print("+" + "-" * largura + "+")
        renderizaSala(sala, fileiras, assentos)

        print("-" * 18)
        print(f"Espectador N° {cadastros + 1}")
        print("-" * 18)

        for f in range(fileiras, 0, -1):
            print(f"[{f}] - Fileira {f}")

        fileiraSelecionada = int(input("Escolha uma fileira disponível:\n> "))

        while fileiraSelecionada not in range(1, fileiras + 1):
            print("Informe uma fileira válida.")
            fileiraSelecionada = int(input("> "))

        print("-" * 18)

        for i in range(1, assentos + 1):
            print(f"[{i}] - Assento {i}")

        assentoLivre = False

        while not assentoLivre:

            assentoSelecionado = int(input("Selecione um assento: "))

            while assentoSelecionado not in range(1, assentos + 1):
                print("Informe um assento válido.")
                assentoSelecionado = int(input("> "))

            for lugar in sala:

                if (
                    lugar[0] == fileiraSelecionada and
                    lugar[1] == assentoSelecionado
                ):

                    if lugar[2]:
                        print("Assento já ocupado! Escolha outro.")
                    else:
                        lugar[2] = True
                        cadastros += 1
                        assentoLivre = True

                        print(
                            f"Assento {assentoSelecionado} "
                            f"da fileira {fileiraSelecionada} reservado."
                        )

                    break
            
            renderizaSala(sala, fileiras, assentos)

            print()
            print("Continuar cadastro? [S/N]")
            escolha = input("> ")
            if(escolha.lower().strip() == 'n'):
                cadastrando = False


    return sala  # retorna a sala com os assentos atualizados
    