def renderizarSalaInicial(fileiras:int, assentos:int):
    sala = []
    # sala ficara como:[[0] fileira e [1] assento]
    # Cabeçalho
    print("  ", end="")
    for assento in range(1, assentos + 1):
        print(f"{assento:^5}", end="")
    print()

    # Fileiras
    for fileira in range(1, fileiras + 1):
        print(f"{fileira:<3}", end="")
        for assento in range(1, assentos + 1):
            print("[ ]  ", end="")
            sala.append([fileira, assento])
        print()
    
    assentosLivres = assentos * fileiras 

    return sala, assentosLivres


def _exec_sala_visual(filmeEscolhido:list):
    print(f"FILME SELECIONADO:")
    titulo = filmeEscolhido[0]

    largura = len(titulo) + 4

    print("+" + "-" * largura + "+")
    print(f"|  {titulo.upper()}  |")
    print("+" + "-" * largura + "+")

    fileiras = filmeEscolhido[3]
    assentos = filmeEscolhido[4]

    sala, assentosDisponiveis = renderizarSalaInicial(fileiras, assentos)
    cadastrando = True
    opcoesFileiras = []
    print()
    print()

    print("=" * 77)
    cadastros = 0

    while cadastros <= assentosDisponiveis:
        cadastros += 1

        print("-" * 18)
        print(f"Espectador N° {cadastros}")
        print("-" * 18)


        while cadastrando:
            for f in range(fileiras, 0, -1):
                print(f'[{f}] Fileira {f}')
                opcoesFileiras.append(f)

            print("Escolha uma fileira dentre as Disponiveis:")
            fileiraSelecionada = int(input("> "))
            fileiraValida = False

            while not fileiraValida:
                if(fileiraSelecionada in opcoesFileiras):
                    fileiraValida = True
                else:
                    print("Informe uma fileira válida.")
                    fileiraSelecionada = int(input("> "))
