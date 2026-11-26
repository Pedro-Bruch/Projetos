import os, time
saldo = 0

historico = []

def clear():
    os.system("cls" if os.name == "nt" else "clear")
    
def depositar():
    global saldo
    saldo += qntd

def saque():
    global saldo
    saldo -= qntd
    
while True:
    print("=" * 50)
    print(f"R$ {saldo}")
    print("=" * 50)
    esc = int(input("1 - Depositar\n2 - Sacar\n3 - Histórico"))
    
    if esc == 1:
        qntd = float(input("Digite quanto deseja depositar(utilize apenas números com duas casas décimais. ex: 01.10): "))
        depositar()
        time.sleep(1)
        clear()
    
    if esc == 2:
        if saldo <= 0:
            print("Você não tem saldo suficiente para realizar um saque.")
        else:
            qntd = float(input("Digite quanto deseja sacar(utilize apenas números com duas casas décimais. ex: 01.10): "))
            historico.append(qntd)
            conta = input("Digite o ID do destinatario: ")
            saque()
            time.sleep(1)
            clear()
    
    if esc == 3:
        