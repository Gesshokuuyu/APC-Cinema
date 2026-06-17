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
    # Pega os dados da sala a partir do filme selecionado
    idSala = filmeEscolhido[2]
    fileiras = filmeEscolhido[3]
    assentos = filmeEscolhido[4]

    # Cria a estrutura inicial da sala e conta os assentos disponíveis
    sala, assentosDisponiveis = renderizarSalaInicial(
        idSala,
        fileiras,
        assentos
    )

    print("\n")
    print("=" * 77)

    # Inicializa as variveis de controle do processo de cadastro de espectadores
    cadastrando = True
    cadastros = 0

    # Continua enquanto houver assentos livres e o usuário desejar cadastrar
    while cadastros < assentosDisponiveis and cadastrando:

        limpaTerminal()

        # Exibe o filme selecionado
        print("FILME SELECIONADO:")
        titulo = filmeEscolhido[0]
        largura = len(titulo) + 4

        print("+" + "-" * largura + "+")
        print(f"|  {titulo.upper()}  |")
        print("+" + "-" * largura + "+")

        # Mostra o mapa atual da sala
        renderizaSala(sala, fileiras, assentos)

        print("-" * 18)
        print(f"Espectador N° {cadastros + 1}")
        print("-" * 18)

        # Lista as fileiras disponíveis
        for f in range(fileiras, 0, -1):
            print(f"[{f}] - Fileira {f}")

        # Solicita a escolha da fileira
        fileiraSelecionada = int(
            input("Escolha uma fileira disponível:\n> ")
        )

        # Valida a fileira informada
        while fileiraSelecionada not in range(1, fileiras + 1):
            print("Informe uma fileira válida.")
            fileiraSelecionada = int(input("> "))

        print("-" * 18)

        # Lista os assentos disponíveis na fileira
        for i in range(1, assentos + 1):
            print(f"[{i}] - Assento {i}")

        assentoLivre = False

        # Continua solicitando assentos até encontrar um livre
        while not assentoLivre:

            assentoSelecionado = int(input("Selecione um assento: "))

            # Valida o número do assento
            while assentoSelecionado not in range(1, assentos + 1):
                print("Informe um assento válido.")
                assentoSelecionado = int(input("> "))

            # Procura o assento escolhido na estrutura da sala
            for lugar in sala:

                if (
                    lugar[0] == fileiraSelecionada and
                    lugar[1] == assentoSelecionado
                ):

                    # Verifica se o assento já está ocupado
                    if lugar[2]:
                        print("Assento já ocupado! Escolha outro.")
                    else:
                        # Reserva o assento
                        lugar[2] = True
                        cadastros += 1
                        assentoLivre = True

                        print(
                            f"Assento {assentoSelecionado} "
                            f"da fileira {fileiraSelecionada} reservado."
                        )

                    break

            # Atualiza a visualização da sala após a reserva
            renderizaSala(sala, fileiras, assentos)

            # Pergunta se deseja continuar cadastrando espectadores
            print()
            print("Continuar cadastro? [S/N]")
            escolha = input("> ")

            if escolha.lower().strip() == 'n':
                cadastrando = False

    # Retorna a sala atualizada com os assentos reservados
    return sala
    