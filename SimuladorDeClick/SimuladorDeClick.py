import random, time, os

#Dados para jogo

itens_equipados = []
ponto = 0
rena = 0
rens = 2
x = 1

if rena >= 1:
    mult = 1 * rens
else:
    mult = 1

quest = 2
pontos_nec = 150
pontos_nec_ren = 30000
pontos_nec_aura = 5000
aura = 1.5

def ponto_novo(ponto):
    i = 0
    while ponto >= 1000:
        ponto = ponto / 1000
        i += 1
    return f"{ponto:.1f}{resum[i]}"

resum = ["","k","M","B","T"]

caixa1 = {
    "Pet comum": [1.55, 40],
    "Pet comum2": [1.85, 33],
    "Pet raro": [2, 20],
    "Pet épico": [3, 5],
    "Pet lendário": [4, 3],
}
caixa2 = {
    "Espada comum": [5.5, 40],
    "Espada comum": [5.8, 33],
    "Espada rara": [6.2, 20],
    "Espada épica": [7, 5],
    "Espada lendária": [8.5, 3],
}
caixa3 = {
    "Armadura de couro": [9, 40],
    "Armadura de ferro": [9.25, 33],
    "Armadura de ouro": [9.7, 20],
    "Armadura de diamante": [10, 5],
    "Armadura de netherite": [11.5, 3],
}
caixa4 = {
    "Enxada de plástico": [14, 40],
    "Pá de pedra": [14.5, 33],
    "Picareta de ferro": [16, 20],
    "Arco encantado": [17, 5],
    "Lança de diamante": [19.5, 3],
}
caixa5 = {
    "Luva de boxe": [20.5, 20],
    "Cacetete": [21, 18],
    "Soco inglês": [21.5, 16],
    "Garrafa quebrada": [23, 10],
    "Pé de cabra": [24, 8],
    "Taco de Beisebol": [25.5, 8],
    "Canivete": [27, 7],
    "Cutello": [28.5, 6],
    "Machete": [29.5, 5],
    "Serra elétrica": [35, 2],
}
caixa6 = {
    "Glock": [36, 37],
    "Espingarda": [38, 22],
    "Escopeta": [39.5, 16],
    "Fuzil": [41, 10],
    "Sniper": [43, 8],
    "Metralhadora": [45, 6],
    "Lança míssil": [37, 1],
}
caixas = {
    1: {
        "preco": 10000,        
        "itens": caixa1
    },
    2: {
        "preco": 100000,
        "itens": caixa2
    },
    3: {
        "preco": 550000,
        "itens": caixa3
    },
    4: {
        "preco": 2650000,
        "itens": caixa4
    },
    5: {
        "preco": 8450000,
        "itens": caixa5
    },
    6: {
        "preco": 15000000,
        "itens": caixa6
    }
}

def clear():
    os.system("cls" if os.name == "nt" else "clear")
    
def voltarMenu():
    print("Voltando ao menu.")
    time.sleep(1)
    clear()

def obter_poder(item_nome):
    """Busca o multiplicador do item dentro de qualquer caixa"""
    for c in caixas.values():
        if item_nome in c["itens"]:
            return c["itens"][item_nome][0]
    return 0

def abrir_caixa(id_caixa):
    global ponto, itens_equipados
    
    dados_da_caixa = caixas[id_caixa]
    preco = dados_da_caixa["preco"]
    dicio_itens = dados_da_caixa["itens"]

    itens = list(dicio_itens.keys())
    pesos = [info[1] for info in dicio_itens.values()]               
    
    girar = input(f"\nRolar = {ponto_novo(preco)} pontos.\nDeseja rolar? (s/n): ").lower()
    
    while girar == 's':
        if ponto < preco:
            print("Pontos insuficientes.")
            time.sleep(1)
            voltarMenu()
            break
        else:
            ponto -= preco
            sort = random.choices(itens, weights=pesos, k=1)[0]
            print("Girando...")
            time.sleep(1)
            print("O item sorteado foi: ", sort)
            
            if len(itens_equipados) < 2:
                itens_equipados.append(sort)
            else:
                candidatos = itens_equipados + [sort]
                candidatos_ordenados = sorted(candidatos, key=obter_poder, reverse=True)                            
                novos_equipados = candidatos_ordenados[:2]
                
                if novos_equipados != itens_equipados:
                    itens_equipados = novos_equipados
            
            print(f"\n\nPontos: {ponto_novo(ponto)}")
            girar = input("\nDeseja rolar novamente? (s/n): ").lower()
            
            if girar == 'n':
                voltarMenu()

def multiplicador():
    mult_itens = 1
    for item in itens_equipados:
        mult_itens += obter_poder(item)
        mult_itens += aura
    return mult * mult_itens

def loja_mudar():
    global quest, pontos_nec
    quest *= 2
    pontos_nec *= 4
    
def aura_mudar():
    global aura, pontos_nec_aura
    aura += 0.5
    pontos_nec_aura *= 2
    
def renascimento():
    global rens, pontos_nec_ren
    rens *= 2
    pontos_nec_ren *= 11         

#Começo do jogo

while True:
    print(f"\n\nPontos: {ponto_novo(ponto)}")
    
    print(f"Multiplicador: {multiplicador():.2f}x")
    pontos = input("1 - Loja\n2 - Renascimento \n3 - Itens\n4 - Auras\n5 - Mochila\nAperte enter para farmar pontos\n")
    
    #Loja de upgrade
    if pontos == '1':
        clear()
        print(f"Upgrades:\n{quest}x = {ponto_novo(pontos_nec)} pontos")
        conf = input("Deseja fazer o upgrade? (s/n): ")
        if conf == 's':
            if ponto >= pontos_nec:                
                ponto -= pontos_nec
                print("Upgrade realizado!")
                mult = quest
                loja_mudar()
                time.sleep(1)
                voltarMenu()
            else:
                print("Erro, pontos insuficientes!")
                time.sleep(1)
                voltarMenu()
        else:
            voltarMenu()
            
    # Renascimento
    if pontos == '2':
        clear()
        print("Renascimento zera os pontos e reseta a loja, mas aumenta o multiplicador base.")
        print(f"\nRenascimento:\n{rens}x = {ponto_novo(pontos_nec_ren)} pontos")
        renas = input("Deseja fazer o renascimento? (s/n): ")
        
        if renas == 's':
            if ponto >= pontos_nec_ren:
                ponto = 0
                print("Renascimento feito!")
                                
                if rena == 0:
                    rena += 1  
                       
                mult = rens                
                quest = 2
                pontos_nec = 150
                
                renascimento()
                time.sleep(1)
                voltarMenu()
            else:
                print("Erro, pontos insuficientes!")
                voltarMenu()
        else:
            voltarMenu()
    
    # Caixa e itens
    if pontos == '3':
        clear()
        print("Caixas de itens")
        caixa_input = input("\n1- Caixa Pet\n2- Caixa Espada\n3- Caixa Armadura\n4- Caixa Minecraft\n5- Caixa Armas Brancas\n6- Caixa Armas de Fogo\nDigite a opção (digite 0 para sair): ")
        
        if caixa_input.isdigit():
            caixa = int(caixa_input)
            if caixa in caixas:
                clear()
                print("Chances: ")
                for item, info in caixas[caixa]["itens"].items():
                    print(f"- {item} ({info[1]}%)")
                abrir_caixa(caixa)
            elif caixa == 0:
                voltarMenu()
            else:
                print("Erro: caixa inexistente.")
                time.sleep(1)
                voltarMenu()                        
        clear()
    
    #aura
    if pontos == '4':
        clear()
        print(f"Auras:\nAura {x}: {aura}x = {ponto_novo(pontos_nec_aura)} pontos")
        aura_esc = input(f"Deseja comprar a aura {x}? (s/n): ").lower()
        
        if aura_esc == 's':
            if ponto >= pontos_nec_aura:
                ponto -= pontos_nec_aura
                print("Aura adquirida!")
                aura_mudar()
                time.sleep(1)
                voltarMenu()          
        
    
    
    # Mochila
    if pontos == '5':
        clear()
        if len(itens_equipados) == 0:
            print("Você não tem nenhum item equipado!")
        else:
            print("Itens Equipados:")
            for item in itens_equipados:
                print(f"- {item} (Poder: {obter_poder(item)})")
        time.sleep(2)
        voltarMenu()
                
    # Click (Farmar pontos)
    if pontos == "":
        ponto += multiplicador()
        clear()