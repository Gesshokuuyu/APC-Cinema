


# sera uma lista onde cada posicao tem mais uma lista, sendo pos 0 ome e pos 1 a duração em minutos
filmes = [
          ["O lobo de WallStreet", '180'],
          ["Todo mundo em Panico 6", "95"], 
          ["Crepusculo", "122"], 
          ["Velozes e Furiosos 2", "107"],
          ["Piratas do Caribe 2", "151"]
        ]

print("-" * 20)
print("")
print("Bem Vindo ao cinema")

print("")
print("FIlmes em cartaz: ")
for filme in filmes:
    print(f"---{filme[0]}---")
    print(f"Duração(minutos): {filme[1]}")
    print("" *3)
