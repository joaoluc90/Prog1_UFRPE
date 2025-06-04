import os
import time
def limpar_tela():
    os.system('cls'if os.name == 'nt'else 'clear')
R = '\033[31m'  # vermelho
G = '\033[32m'  # verde
B = '\033[34m'  # azul
Y = '\033[33m'  # amarelo
P = '\033[35m'  # roxo
C = '\033[36m'  # ciano
W = '\033[37m'  # branco
i = '\033[3m'   # itálico
n = '\033[7m'   # negativo
r = '\033[0m'   # resetar
p = "\033[F"    # mover o cursor para o começo da linha anterior
u = "\033[A"    # mover o cursor para cima uma linha
meses = ["janeiro", "fevereiro", "março", "abril", "maio", "junho",
"julho", "agosto", "setembro", "outubro", "novembro", "dezembro"]
mes_atual = 5 
ano_atual = 2025
class Investimento:
    def __init__(self, percentual, aporte, recorrente):
        self.percentual = percentual
        self.aporte = aporte
        self.recorrente = recorrente == 'sim'
        self.total_investido = aporte
        self.saldo = aporte
        self.resgate = 0
primeiro_mes = True
print("[SIMULADOR DE INVESTIMENTOS RECORRENTES]")
time.sleep(1.0)
print()
print(f"{i}Bem vindo, vamos simular também investimentos recorrentes!")
print("Neste exercício vamos usar somente LCIs, sem cálculo de IR dessa vez")
time.sleep(1.0)
print()
print(f"Iniciando as simulações...{r}")
time.sleep(2.0)
print()
investimentos = []
while True:
    menu = input(f"Digite [{B}novo{r}] investimento, [{B}sair{r}] ou aperte [{B}enter{r}] para avançar em um mês: ").lower().strip()
    if menu == 'novo':
        limpar_tela()
        try:
            percentual = int(input(f"Qual o percentual? ({B}% do CDI{r}): "))
            aporte = int(input(f"Qual o {B}valor{r} do aporte de entrada? "))
            recorrente = input(f"Serão depósitos mensalmente recorrentes? ({B}sim/não{r}): ").lower().strip()
        except ValueError:
            print(f"{R}⚠️ Entrada inválida. Tente novamente.{r}")
            input("Pressione enter para continuar...")
            limpar_tela()
            continue
        novo_invest = Investimento (float(percentual), float(aporte), recorrente)
        investimentos.append(novo_invest)
        print()
        print(f"{i}Investimento adicionado com sucesso!{r}")
        time.sleep(2.0)
        limpar_tela()
        continue
    elif menu == 'sair':
        print("Ok, finalizando a simulação...")
        time.sleep(2.0)
        break
    elif menu == '':
        limpar_tela()
        print("[SIMULAÇÃO]")
        cdi = float("14.65")
        cdi_decimal = cdi / 100
        taxa_mensal = (1 + cdi_decimal) ** (1/12) - 1
        print()
        for inv in investimentos:
            if inv.recorrente and not primeiro_mes:
                inv.saldo += inv.aporte
                inv.total_investido += inv.aporte
            rendimento = inv.saldo * (taxa_mensal * (inv.percentual / 100))
            inv.saldo += rendimento
            inv.resgate = inv.saldo - inv.total_investido
            tipo = 'R' if inv.recorrente else 'U'
            simbolos = "$" * int(inv.saldo // 1000)
            alinhado = f"[{tipo}][LCI de {inv.percentual:6.2f}% do CDI {Y}R${inv.total_investido:10.2f}{r}, {G}R${inv.saldo:10.2f}{r}]\t"
            print(f"{alinhado:<70}{G}{simbolos}{r}")
        print(f"{i}Resumo da simulação em {P}{meses[mes_atual]} de {ano_atual}{r}")
        print()
        print("...")
        print()
        mes_atual += 1
        if mes_atual == 12:
            mes_atual = 0
            ano_atual += 1
        primeiro_mes = False
        continue