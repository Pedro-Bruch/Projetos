import os, time, json
from datetime import datetime

saldo = 0
ARQUIVO = "historico.json"

def clear():
    os.system("cls" if os.name == "nt" else "clear")
    
def depositar(valor):
    global saldo
    saldo += qntd

def saque(valor):
    global saldo
    saldo -= qntd

def carregar_historico():
    try:
        with open(ARQUIVO, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def historico(valor):
    conta = input("Identificação do saque: ")
    agr = datetime.now().astimezone()
    
    novo_registro = {
        "data_hora": agr.isoformat(),
        "data_formatada": agr.strftime("%d/%m/%Y %H:%M:%S"),
        "valor": valor,
        "frase": conta
    }

    lista_historico = carregar_historico()
    lista_historico.append(novo_registro)
    
    with open(ARQUIVO, "w", encoding="utf-8") as f:
        json.dump(lista_historico, f, ensure_ascii=False, indent=2)
    
while True:
    print("=" * 50)
    print(f"R$ {saldo}")
    print("=" * 50)
    esc = int(input("1 - Depositar\n2 - Sacar\n3 - Histórico\n"))
    
    if esc == 1:
        qntd = float(input("Digite quanto deseja depositar(utilize apenas números com duas casas décimais. ex: 01.10): "))
        depositar(qntd)
        time.sleep(1)
    if esc == 2:
        qntd = float(input("Digite quanto deseja sacar (ex: 10.50): "))
        if qntd > saldo:
            print("Você não tem saldo suficiente para realizar esse saque.")
            time.sleep(2)
            clear()
        else:
            historico(qntd)
            saque(qntd)
            time.sleep(1)
            clear()
    
    if esc == 3:
        clear()
        print("=" * 50)
        print("HISTÓRICO DE REGISTROS")
        print("=" * 50)
        lista_historico = carregar_historico()
        
        if not lista_historico:
            print("Nenhum registro encontrado.")
        else:
            for i, item in enumerate(lista_historico, start=1):
                print(f"{i}. [{item['data_formatada']}] - R$ {item['valor']:.2f} | {item['frase']}")
        
        input("\nPressione Enter para voltar ao menu...")
        clear()

        