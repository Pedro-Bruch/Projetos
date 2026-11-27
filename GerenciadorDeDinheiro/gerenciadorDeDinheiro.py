import os, time, json
from datetime import datetime

saldo = 0
ARQUIVO = "historico.json"
ARQUIVO2 = "usuarios.json"

def cadastrar(usuario, senha):
    try:
        with open(ARQUIVO2, "r", encoding="utf-8") as f:
            for linha in f:
                user_salvo, _, _ = linha.strip().split(":")
                if user_salvo == usuario:
                    return False
    except FileNotFoundError:
        pass

    
    with open(ARQUIVO2, "a", encoding="utf-8") as f:
        f.write(f"{usuario}:{senha}:0\n")
    return True


def login(usuario, senha):
    try:
        with open(ARQUIVO2, "r", encoding="utf-8") as f:
            for linha in f:
                user_salvo, senha_salva, saldo = linha.strip().split(":")
                if user_salvo == usuario and senha_salva == senha:
                    return float(saldo)
    except FileNotFoundError:
        return None
    return None  

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
    logar = int(input("1 - Login\n2 - Cadastro\n"))
    if logar == 1:
        usuario = input("Digite o Usuário: ")
        senha = input("Digite a Senha: ")
        if login(usuario, senha):
            print("Logado com sucesso!")
        else:
            print("Usuário ou senha incorretos.")
        time.sleep(1)
        clear()
    
    if logar == 2:
        usuario = input("Digite o Usuário: ")
        senha = input("Digite a Senha: ")
        
        if cadastrar(usuario, senha):
            print("Cadastrado!")
        else:
            print("Usuário já existe.")
        time.sleep(1)
        clear()
        
    print("=" * 50)
    print(f"Olá {usuario},\nR$ {saldo}")
    print("=" * 50)
    esc = int(input("1 - Depositar\n2 - Sacar\n3 - Histórico\n4 - Sair\n"))
    
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
    
    if esc == 4:
        break

        