import os
from dados_dos_dois import *
from simulacao import simular_mercado

roxo = '\033[35m'
azul = '\033[34m'
verde = '\033[32m'
ciano = '\033[96m'
amarelo = '\033[93m'
vermelho = '\033[31m'
italico = '\033[3m'
reset = '\033[0m' 

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def print_pessoas(pessoas, mostrar_conforto=True):
    
    print(f"\n[PESSOAS]")
    divisao = f"Divisão do renda mensal | Moradia {amarelo}{percentuais[0]*100:.1f}%{reset} | Alimentação {amarelo}{percentuais[1]*100:.1f}%{reset} | Transporte {amarelo}{percentuais[2]*100:.1f}% {reset} | Saúde {amarelo}{percentuais[3]*100:.1f}%{reset} | Educação {amarelo}{percentuais[4]*100:.1f}%{reset} | Totalizando {amarelo}{sum(percentuais)*100:.1f}%{reset} da renda mensal total."
    print(f"{italico}{divisao}{reset}{reset}")
    print(f"{italico}Gráfico de Barras | Legenda: {italico}{azul}Conforto{reset}{italico}, {verde}Salário{reset}{italico}, {roxo}Rendimentos{reset}{italico} | Cada traço = R$1000.00{reset}\n")

    
    conforto_linhas = []
    rendimento_linhas = []

    for p in pessoas:
        conforto_barras = min(int(round((p.conforto / len(percentuais)))), 10)
        conforto_linhas.append([azul + "|" + reset] * conforto_barras)
    
        rendimento_do_patrimonio = p.patrimonio * 0.05
        salario = p.salario
        total_rendimento = salario + rendimento_do_patrimonio
        total_barras = min(int(total_rendimento // 1000), 10)

        barras_salario = min(int(salario // 1000), total_barras)
        barras_patrimonio = total_barras - barras_salario

        barras = [roxo + "|" + reset] * barras_patrimonio + [verde + "|" + reset] * barras_salario
        rendimento_linhas.append(barras)

    if mostrar_conforto:
        for nivel in reversed(range(10)):
            linha = ""
            for barras in conforto_linhas:
                linha += barras[nivel]  if nivel < len(barras) else " "
            print(linha)

        print(("----") * 40)

    for nivel in reversed(range(10)):
        linha = ""
        for barras in rendimento_linhas:
                linha += barras[nivel] if nivel < len(barras) else " "
        print(linha)
            

def mostrar_vendas(vendas, limite_sinais=10):
    if vendas < 5:
        return ""
    
    quantidade_de_sinais = vendas // 5
    if quantidade_de_sinais > limite_sinais:
        exedente = quantidade_de_sinais - limite_sinais
        return verde + ("$" * limite_sinais) + f"+{exedente}" + reset
    
    else:
        return verde + ("$" * quantidade_de_sinais) + reset
    
    
def print_empresas(empresas):
    print(f"\n[EMPRESAS]")
    for empresa in empresas:
        preco = empresa.o_preco()
        cat = f"[{empresa.categoria}]"
        nome_prod = f"{empresa.nome}: {empresa.produto}"
        qual_marg = f"{ciano}Q:{empresa.qualidade}{reset} Margem: {amarelo}{empresa.margem:.1%}{reset}"
        custo_str = f"Custo:{vermelho} R$ {empresa.custo:<8.2f}{reset}"
        preco_str = f"Preço:{verde} R$ {preco:<8.2f}{reset}"
        lucro_str = f"Lucro T.:{verde} R$ {empresa.lucro_total:<8.2f}{reset}"
        vendas_str = f"Vendas: {mostrar_vendas(empresa.vendas)}"
        
        print(f"{cat:<14}{nome_prod:<32}{qual_marg:<28}        {custo_str:<27}        {preco_str:<27}        {lucro_str:<25}         {vendas_str}{reset}")


def main():
    pessoas_aleatorias()
    tabela_de_empresas()

    meses_simulando = 0

    
    clear()
    print("[SIMULADOR DE RELAÇÕES DE MERCADO]")
    if meses_simulando > 0:
            print(f"Simulação após {meses_simulando} meses.")
    print_pessoas(pessoas, mostrar_conforto=False)
    print_empresas(empresas)

    

    
    while True:
        if meses_simulando > 0:
            print(f"Simulação após {meses_simulando} meses.")
        resposta = input(f"\nDigite um número para avançar N meses, 'enter' para avançar 1 mês ou 'sair' para encerrar: ")

        if resposta.isdigit():
            meses = int(resposta)
            for _ in range(meses):
                simular_mercado(pessoas, empresas, categorias, percentuais)
            meses_simulando += meses
        elif resposta == "":
            simular_mercado(pessoas, empresas, categorias, percentuais)
            meses_simulando += 1
        elif resposta == "sair":
            break
        else:
            continue
        
        clear()
        print("[SIMULADOR DE RELAÇÕES DE MERCADO]")
        if meses_simulando > 0:
            print(f"Simulação após {meses_simulando} meses.")
        print_pessoas(pessoas)
        print_empresas(empresas)

        

if __name__ == "__main__":
    main()
