import os
def clear():
    os.system('cls'if os.name == 'nt' else 'clear')
import tkinter as tk
from tkinter import ttk
from tkinter import Scrollbar
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import sys

# Códigos das cores de texto em Python
R = '\033[31m' # vermelho
G = '\033[32m' # verde
B = '\033[34m' # azul
Y = '\033[33m' # amarelo
P = '\033[35m' # roxo
C = '\033[36m' # ciano
W = '\033[37m' # branco
i = '\033[3m'  # itálico
n = '\033[7m'  # negativo
r = '\033[0m'  # resetar
p = "\033[F"   # mover o cursor para o começo da linha anterior
u = "\033[A"   # mover o cursor para cima uma linha

# Parte 1, classe pessoa
class Pessoa:
    def __init__(self, patrimonio, salario):
        self.patrimonio = patrimonio
        self.conforto = 0.0
        self.salario = salario

class Empresa:
    def __init__(self, categoria, nome, produto, custo, qualidade):
        self.nome = nome
        self.categoria = categoria
        self.produto = produto
        self.custo = custo
        self.qualidade = qualidade
        self.margem = 0.05
        self.oferta = 0
        self.reposicao = 10
        self.vendas = 0

pessoas = []
empresas = []
categorias = [
    "Moradia", 
    "Alimentação", 
    "Transporte", 
    "Saúde", 
    "Educação"
]

percentuais = [
    0.35,  # Moradia
    0.25,  # Alimentação
    0.10,  # Transporte
    0.10,  # Saúde
    0.10,  # Educação
]

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def add_pessoas(num_pessoas, patrimonio, salario, variacao=0.0):
    for i in range(num_pessoas):
        pessoas.append(Pessoa(patrimonio + i * variacao, salario + i * variacao))

def calc_preco(empresa):
    return empresa.custo * (1 + empresa.margem)

def calc_disponibilidade(empresa):
    if empresa.oferta > 0:
        return True
    else:
        return False

def comprar(pessoa, empresa):
    empresa.vendas += 1
    empresa.oferta -= 1
    pessoa.patrimonio -= calc_preco(empresa)
    pessoa.conforto += empresa.qualidade

# Pesquisar melhor produto de uma categoria 
def escolher_melhor(categoria, empresas, orcamento):
    melhor_empresa = None
    for empresa in empresas:
        if empresa.categoria == categoria and empresa.oferta > 0:
            preco = calc_preco(empresa)
            if preco <= orcamento:
                if melhor_empresa is None or empresa.qualidade > melhor_empresa.qualidade:
                    melhor_empresa = empresa
                elif empresa.qualidade == melhor_empresa.qualidade:
                    if calc_preco(empresa) < calc_preco(melhor_empresa):
                        melhor_empresa = empresa

    return melhor_empresa

# Pesquisar produto mais barato de uma categoria 
def escolher_barato(categoria, empresas, orcamento):
    melhor_empresa = None
    for empresa in empresas:
        if empresa.categoria == categoria and empresa.oferta > 0:
            preco = calc_preco(empresa)
            if preco <= orcamento:
                if melhor_empresa is None or preco < calc_preco(melhor_empresa):
                    melhor_empresa = empresa

    return melhor_empresa

# Calcular a renda mensal total da pessoa, incluindo renda passiva
def calc_renda_mensal(pessoa):
    return pessoa.salario + (pessoa.patrimonio * 0.005)

def simular_empresa(empresa):
    # Se a oferta zerou quer dizer que a empresa vendeu tudo
    if empresa.oferta == 0:
        empresa.reposicao += 1
        empresa.margem += 0.01

    # Se a oferta está alta, quer dizer que as vendas foram aquém
    elif empresa.oferta > 10:
        empresa.reposicao = max(0, empresa.reposicao - 1)
        if(empresa.margem > 0.01):
            empresa.margem -= 0.01

    # Repor o estoque de produtos
    empresa.oferta += empresa.reposicao  # Exemplo de reposição de estoque
    empresa.vendas = 0  # Resetar vendas após reposição

def simular_pessoa(pessoa, empresas, categorias, percentuais):
    # Reinicializar conforto da pessoa
    pessoa.conforto = 0.0

    # Fazer compras dentro do orçamento para cada categoria
    # e atualizar o conforto da pessoa

    # Renda passiva
    # Aplicar o percentual de rendimento no patrimônio da pessoa como renda passiva
    renda_total = calc_renda_mensal(pessoa)

    pessoa.patrimonio += renda_total  # Atualizar patrimônio com a renda total

    for categoria in categorias:
        # Comprar o produto de melhor qualidade 
        # que caiba no orçamento da pessoa para aquela categoria
        percentual = percentuais[categorias.index(categoria)]
        orcamento = renda_total * percentual
        patrimonio = pessoa.patrimonio
        empresa = escolher_melhor(categoria, empresas, orcamento)
        if empresa is None:
            empresa = escolher_barato(categoria, empresas, patrimonio)

        # Se encontrou um produto, comprar e atualizar o conforto
        if empresa is not None:
            comprar(pessoa, empresa)

def simular_mercado(pessoas, empresas, categorias, percentuais):
    # Atualização das empresas e produtos
    for empresa in empresas:
        simular_empresa(empresa)

    # Atualização das pessoas e seus patrimônios
    for pessoa in pessoas:
        simular_pessoa(pessoa, empresas, categorias, percentuais)        

def print_pessoas(pessoas):
    print()
    print("[PESSOAS]")

    # Imprimir em uma linha os percentuais dedicados à cada categoria
    print(f"{i}Divisão da renda mensal ", end="")
    for categoria, percentual in zip(categorias, percentuais):
        print(f"| {categoria} ", end="")
        print(f"{Y}{percentual * 100:3.1f}%{r}{i} ", end="")
    soma = sum(percentuais)
    print(f"{i} | Totalizando {Y}{soma * 100:3.1f}%{r}{i} da renda mensal total.{r}")

    # Imprimir as pessoas e seus patrimônios
    max_renda_total = int(max(calc_renda_mensal(p) for p in pessoas))
    max_renda_total = 10000
    step = max_renda_total // 10

    print(f"{i}Gráfico de Barras | Legenda: {B}Conforto{r}{i}, {G}Salário{r}{i}, {P}Rendimentos{r}", end="")
    print(f"{i} | Cada traço = R${step:.2f}{r}{B}")

    for conforto in range(10, 1, -1):
        for pessoa in pessoas:
            char = " "
            if pessoa.conforto // len(categorias) >= conforto:
                char = "|"
            print(char, end="")
        print()

    print(f"{r}", end="")
    for pessoa in pessoas:
        print("-", end="")
    print()

    for renda_total in range(step, max_renda_total, step):
        for pessoa in pessoas:
            char = " "
            if calc_renda_mensal(pessoa) >= renda_total:
                if pessoa.salario >= renda_total:
                    char = f"{G}|{r}"
                else:
                    char = f"{P}|{r}"
            print(char, end="")
        print()
    print(f"{r}", end="")

def print_empresas(empresas):
    print()
    print("[EMPRESAS]")

    for empresa in empresas:
        print(f"|{empresa.categoria}| \t"
              f"{empresa.nome}: {empresa.produto} "
              f"{C}Q={empresa.qualidade}{r} Margem: {Y}{empresa.margem * 100:3.1f}%{r}\t"
              f"Custo: {R}R$ {empresa.custo:.2f}{r}\t"
              f"Preço: {G}R$ {calc_preco(empresa):.2f}{r}\t"
              f"Lucro T.: {G}R$ {(empresa.vendas * empresa.custo * empresa.margem):.2f}{r}\t"
              f"Vendas: ", end="")
        
        for i in range(empresa.vendas // 5):
            print(f"{G}${r}", end="")

        print()

# Parte 2, inicialização do mercado, pessoas e empresas
add_pessoas(5,  patrimonio=20000000, salario=0,      variacao=0)     # Herdeiros milionários
add_pessoas(10, patrimonio=200000,   salario=100000, variacao=-5000) # Supersalários
add_pessoas(25, patrimonio=100000,   salario=30000,  variacao=-1000) # Faixa salarial média-alta
add_pessoas(50, patrimonio=10000,    salario=5000,   variacao=-50)   # Faixa salarial baixa
add_pessoas(70, patrimonio=10000,    salario=1518,   variacao=0)     # Salário mínimo

empresas.append(Empresa("Moradia",     "    República A", "Aluguel, Várzea", 300.0,  qualidade=3))
empresas.append(Empresa("Moradia",     "    República B", "Aluguel, Várzea", 300.0,  qualidade=3))
empresas.append(Empresa("Moradia",     "CTI Imobiliária", "Aluguel, Centro", 1500.0, qualidade=7))
empresas.append(Empresa("Moradia",     "Orla Smart Live", "Aluguel, Boa V.", 3000.0, qualidade=9))
empresas.append(Empresa("Alimentação", "          CEASA", "Feira do Mês   ", 200.0,  qualidade=3))
empresas.append(Empresa("Alimentação", "    Mix Matheus", "Feira do Mês   ", 900.0,  qualidade=5))
empresas.append(Empresa("Alimentação", "  Pão de Açúcar", "Feira do Mês   ", 1500.0, qualidade=7))
empresas.append(Empresa("Alimentação", "      Home Chef", "Chef em Casa   ", 6000.0, qualidade=9))
empresas.append(Empresa("Transporte",  "  Grande Recife", "VEM  Ônibus    ", 150.0,  qualidade=3))
empresas.append(Empresa("Transporte",  "           UBER", "Uber Moto      ", 200.0,  qualidade=4))
empresas.append(Empresa("Transporte",  "             99", "99 Moto        ", 200.0,  qualidade=4))
empresas.append(Empresa("Transporte",  "            BYD", "BYD Dolphin    ", 3000.0, qualidade=8))
empresas.append(Empresa("Saúde",       "    Health Coop", "Plano de Saúde ", 200.0,  qualidade=2))
empresas.append(Empresa("Saúde",       "        HapVida", "Plano de Saúde ", 650.0,  qualidade=5))
empresas.append(Empresa("Saúde",       " Bradesco Saúde", "Plano de Saúde ", 800.0,  qualidade=5))
empresas.append(Empresa("Saúde",       "     Sulamérica", "Plano de Saúde ", 850.0,  qualidade=5))
empresas.append(Empresa("Educação",    "      Escolinha", "Mensalidade    ", 100.0,  qualidade=1))
empresas.append(Empresa("Educação",    "     Mazzarello", "Mensalidade    ", 1200.0, qualidade=6))
empresas.append(Empresa("Educação",    "      Arco Íris", "Mensalidade    ", 1800.0, qualidade=8))
empresas.append(Empresa("Educação",    "Escola do Porto", "Mensalidade    ", 5000.0, qualidade=9))

def iniciar_interface():
    root = tk.Tk()
    root.title("Simulador de Relações de Mercado")

    titulo_label = tk.Label(root, text="SIMULADOR DE RELAÇÕES DE MERCADO", font=("Segoe UI", 18, "bold"), fg="blue")
    titulo_label.pack(pady=10)

    meses_simulados = tk.IntVar(value=0)

    style = ttk.Style()
    style.configure("TNotebook.Tab", font=('Segoe UI', 12, 'bold'), padding=[20, 10])

    notebook = ttk.Notebook(root)
    notebook.pack(pady=10, fill="both", expand=True)

    aba_categorias = tk.Frame(notebook)
    aba_pessoas = tk.Frame(notebook)
    aba_empresas = tk.Frame(notebook)
    aba_graficos = tk.Frame(notebook)

    notebook.add(aba_categorias, text="Categorias")
    notebook.add(aba_pessoas, text="Pessoas")
    notebook.add(aba_empresas, text="Empresas")
    notebook.add(aba_graficos, text="Gráficos")

    style.configure("Treeview", font=('Segoe UI', 12))  
    style.configure("Treeview.Heading", font=('Segoe UI', 13, 'bold')) 

    texto_categorias = tk.Text(aba_categorias, wrap="word")
    tree_pessoas = ttk.Treeview(aba_pessoas, columns=("nome", "patrimonio", "salario", "renda", "conforto"), show="headings")
    tree_pessoas.heading("nome", text="Nome")
    tree_pessoas.heading("patrimonio", text="Patrimônio")
    tree_pessoas.heading("salario", text="Salário")
    tree_pessoas.heading("renda", text="Renda Mensal")
    tree_pessoas.heading("conforto", text="Conforto")

    tree_pessoas.column("nome", width=200)
    tree_pessoas.column("patrimonio", width=120, anchor="center")
    tree_pessoas.column("salario", width=100, anchor="center")
    tree_pessoas.column("renda", width=120, anchor="center")
    tree_pessoas.column("conforto", width=80, anchor="center")

    scrollbar = Scrollbar(aba_pessoas, orient="vertical", command=tree_pessoas.yview)
    tree_pessoas.configure(yscrollcommand=scrollbar.set)
    scrollbar.pack(side="right", fill="y")
    tree_pessoas.pack(expand=True, fill="both")

    texto_empresas = tk.Text(aba_empresas, wrap="word")
    texto_graficos = tk.Text(aba_graficos, wrap="word")

    fonte_texto = ("consolas", 20)

    for t in [texto_categorias, texto_empresas, texto_graficos]:
        t.configure(font=fonte_texto)
        t.pack(expand=True, fill="both")

    def simular_mes():
        simular_mercado(pessoas, empresas, categorias, percentuais)
        meses_simulados.set(meses_simulados.get() + 1)

        texto_categorias.delete("1.0", tk.END)
        texto_empresas.delete("1.0", tk.END)
        plt.close('all') 
        fig, axs = plt.subplots(2, 1, figsize=(9, 4), dpi=100, height_ratios=[2, 1])
        for widget in aba_graficos.winfo_children():
            widget.destroy()

        fig, axs = plt.subplots(2, 1, figsize=(9, 4), dpi=100, height_ratios=[2, 1])

        pessoas_ordenadas = sorted(pessoas, key=lambda p: p.salario + (p.patrimonio * 0.005), reverse=True)

        salarios = [p.salario for p in pessoas_ordenadas]
        rendimentos = [p.patrimonio * 0.005 for p in pessoas_ordenadas]
        confortos = [p.conforto for p in pessoas_ordenadas]
        x = list(range(len(pessoas)))

        axs[0].bar(x, salarios, color="green", label="Salário")
        axs[0].bar(x, rendimentos, bottom=salarios, color="violet", label="Rendimentos")
        axs[0].legend()
        axs[0].set_ylabel("R$")

        axs[1].bar(x, confortos, color="skyblue", label="Nível de Conforto")
        axs[1].set_ylabel("Conforto")
        axs[1].legend()

        plt.tight_layout()

        canvas = FigureCanvasTkAgg(fig, master=aba_graficos)
        canvas.draw()
        canvas.get_tk_widget().pack(expand=True, fill="both")

        texto_categorias.insert(tk.END, "Divisão fixa da renda mensal por categoria:\n\n")
        soma = 0
        for cat, pct in zip(categorias, percentuais):
            texto_categorias.insert(tk.END, f"  - {cat:<12}: {pct*100:.1f}%\n")
            soma += pct
        texto_categorias.insert(tk.END, f"\nTotal utilizado da renda mensal: {soma*100:.1f}%")


        tree_pessoas.delete(*tree_pessoas.get_children())
        nomes_aleatorios = [
            "Ana Beatriz", "Carlos Eduardo", "Mariana Silva", "Lucas Pereira", "Juliana Souza", "Felipe Rocha",
            "Camila Mendes", "Bruno Oliveira", "Larissa Martins", "Diego Fernandes", "Renata Lima", "Gustavo Araujo",
            "Isabela Alves", "Tiago Ramos", "Letícia Freitas", "André Carvalho", "Bruna Santos", "Fernando Dias",
            "Débora Barros", "João Vitor", "Jéssica Castro", "Matheus Lima", "Caroline Ribeiro", "Rafael Costa",
            "Vitória Almeida", "Pedro Henrique", "Aline Rocha", "Marcelo Gomes", "Bianca Silva", "Igor Fernandes",
            "Thais Oliveira", "Eduardo Martins", "Natália Souza", "Leandro Freitas", "Sabrina Costa", "Ricardo Moura",
            "Fernanda Monteiro", "Alexandre Lima", "Yasmin Ferreira", "Rodrigo Alves", "Patrícia Dias", "Vinícius Rocha",
            "Helena Batista", "Thiago Medeiros", "Amanda Vasconcelos", "Gabriel Leal", "Cláudia Teixeira", "Anderson Duarte",
            "Nicole Andrade", "Fábio Campos", "Luciana Vieira", "Paulo Sérgio", "Tatiane Moura", "Wesley Ferreira",
            "Elaine Moreira", "José Augusto", "Raquel Ramos", "Henrique Nunes", "Michele Camargo", "Daniel Souza",
            "Lorena Mendes", "Caio Oliveira", "Talita Gomes", "Rogério Barbosa", "Daniele Santos", "Murilo Castro",
            "Priscila Cunha", "Bruno César", "Érica Machado", "Leonardo Almeida", "Silvana Carvalho", "André Luiz",
            "Gisele Pereira", "Danilo Dias", "Viviane Rezende", "Gilberto Martins", "Vanessa Rocha", "Otávio Ribeiro",
            "Aline Costa", "Marcos Paulo", "Simone Tavares", "Evandro Moreira", "Juliane Teixeira", "Vitor Hugo",
            "Rebeca Ramos", "Samuel Duarte", "Tatiane Alves", "Jefferson Silva", "Kelly Oliveira", "Murilo Sampaio",
            "Lucilene Lima", "João Pedro", "Cristiane Souza", "Renan Pereira", "Ingrid Monteiro", "César Augusto",
            "Kátia Andrade", "Hugo Moura", "Nathália Lopes", "Douglas Carvalho", "Daniela Freitas", "Bruno Henrique",
            "Marina Castro", "Giovani Oliveira", "Beatriz Lima", "Felipe Augusto", "Vivian Rocha", "Heitor Teixeira",
            "Claudia Almeida", "Matheus Costa", "Carla Batista", "Igor Vieira", "Lorraine Silva", "Rafael Nogueira",
            "Paula Gonçalves", "Renato Monteiro", "Juliane Campos", "Humberto Almeida", "Lívia Moura", "Alan Santos",
            "Rafaela Cardoso", "Adriano Souza", "Graziella Ribeiro", "Thiago Freitas", "Emanuelle Lima", "Caio Nascimento",
            "Gabriela Rocha", "Leandro Azevedo", "Caroline Dias", "Marcelo Cunha", "Flávia Medeiros", "Erick Fernandes",
            "Letícia Braga", "Sandro Silva", "Tatiana Lopes", "Paulo Victor", "Ariane Costa", "Bruno Ramos",
            "Luana Teixeira", "Cauã Moura", "Tainá Almeida", "Guilherme Rocha", "Daniela Lopes", "Murilo Silva",
            "Mônica Ferreira", "Antônio Neto", "Rosana Martins", "Lucas Tavares", "Lilian Camargo", "André Lima",
            "Juliana Ribeiro", "Eduardo Souza", "Patrícia Gomes", "Rodrigo Castro", "Rayssa Martins", "Alex Menezes",
            "Tamires Souza", "Wellington Costa", "Júlia Mendes", "Jonathan Freitas", "Larissa Cardoso", "Henrique Rocha",
            "Letícia Nogueira", "Marcelo Silva", "Ariana Souza", "Fábio Mendes", "Amanda Lima", "Hugo Oliveira"
            ]

        for i, p in enumerate(pessoas):
            nome = nomes_aleatorios[i]

            patrimonio = f"R$ {p.patrimonio:,.2f}"
            salario = f"R$ {p.salario:,.2f}"
            renda = f"R$ {calc_renda_mensal(p):,.2f}"
            conforto = f"{p.conforto:.1f}"
            tree_pessoas.insert("", "end", values=(nome, patrimonio, salario, renda, conforto))


        texto_empresas.insert(tk.END, "EMPRESAS:\n")
        for e in empresas[:20]:
                texto_empresas.insert(tk.END,
                    f"{e.nome:20} | {e.produto:15} | Preço: R${calc_preco(e):.2f} | Estoque: {e.oferta} | Margem: {e.margem*100:.1f}%\n"
                )

    botoes_frame = tk.Frame(root, height=70)
    botoes_frame.pack(side="bottom", fill="x", pady=5)
    botoes_frame.pack_propagate(False) 

    left_frame = tk.Frame(botoes_frame)
    left_frame.pack(side="left", padx=10)

    tk.Label(left_frame, text="Meses simulados:").pack(side="left")
    tk.Label(left_frame, textvariable=meses_simulados).pack(side="left", padx=(0, 20))

    tk.Button(left_frame, text="Avançar 1 mês", command=simular_mes, height=2).pack(side="left", padx=5)
    tk.Button(left_frame, text="Sair", command=root.destroy, height=2).pack(side="left", padx=5)


    def resetar_simulacao():
        global pessoas, empresas
        pessoas.clear()
        empresas.clear()
        add_pessoas(5, 20000000, 0, 0)
        add_pessoas(10, 200000, 100000, -5000)
        add_pessoas(25, 100000, 30000, -1000)
        add_pessoas(50, 10000, 5000, -50)
        add_pessoas(70, 10000, 1518, 0)

        empresas.extend([
            Empresa("Moradia",     "    República A", "Aluguel, Várzea", 300.0,  qualidade=3),
            Empresa("Moradia",     "    República B", "Aluguel, Várzea", 300.0,  qualidade=3),
            Empresa("Moradia",     "CTI Imobiliária", "Aluguel, Centro", 1500.0, qualidade=7),
            Empresa("Moradia",     "Orla Smart Live", "Aluguel, Boa V.", 3000.0, qualidade=9),
            Empresa("Alimentação", "          CEASA", "Feira do Mês   ", 200.0,  qualidade=3),
            Empresa("Alimentação", "    Mix Matheus", "Feira do Mês   ", 900.0,  qualidade=5),
            Empresa("Alimentação", "  Pão de Açúcar", "Feira do Mês   ", 1500.0, qualidade=7),
            Empresa("Alimentação", "      Home Chef", "Chef em Casa   ", 6000.0, qualidade=9),
            Empresa("Transporte",  "  Grande Recife", "VEM  Ônibus    ", 150.0,  qualidade=3),
            Empresa("Transporte",  "           UBER", "Uber Moto      ", 200.0,  qualidade=4),
            Empresa("Transporte",  "             99", "99 Moto        ", 200.0,  qualidade=4),
            Empresa("Transporte",  "            BYD", "BYD Dolphin    ", 3000.0, qualidade=8),
            Empresa("Saúde",       "    Health Coop", "Plano de Saúde ", 200.0,  qualidade=2),
            Empresa("Saúde",       "        HapVida", "Plano de Saúde ", 650.0,  qualidade=5),
            Empresa("Saúde",       " Bradesco Saúde", "Plano de Saúde ", 800.0,  qualidade=5),
            Empresa("Saúde",       "     Sulamérica", "Plano de Saúde ", 850.0,  qualidade=5),
            Empresa("Educação",    "      Escolinha", "Mensalidade    ", 100.0,  qualidade=1),
            Empresa("Educação",    "     Mazzarello", "Mensalidade    ", 1200.0, qualidade=6),
            Empresa("Educação",    "      Arco Íris", "Mensalidade    ", 1800.0, qualidade=8),
            Empresa("Educação",    "Escola do Porto", "Mensalidade    ", 5000.0, qualidade=9),
        ])

        meses_simulados.set(0)
        simular_mes()

    right_frame = tk.Frame(botoes_frame)
    right_frame.pack(side="right", padx=10)

    btn_resetar = tk.Button(right_frame, text="Resetar Simulação", command=resetar_simulacao, bg="red", fg="white", font=("Segoe UI", 10, "bold"), height=2)
    btn_resetar.pack()

    entrada_meses = tk.Entry(left_frame, width=5)
    entrada_meses.pack(side="left", padx=5)
    entrada_meses.insert(0, "10")

    def simular_n_meses():
        try:
            n = int(entrada_meses.get())
            if n <= 0:
                raise ValueError("Digite um número positivo.")
            for _ in range(n):
                simular_mes()
                root.update() 
        except ValueError:
            print("Número inválido de meses.")

    tk.Button(left_frame, text="Simular N Meses", command=simular_n_meses).pack(side="left", padx=5)

    simular_mes()
    root.mainloop()
    sys.exit()

def escolher_interface():
    print("Escolha o tipo de interface:")
    print("1 - Console")
    print("2 - Gráfica (Tkinter)")
    escolha = input("Digite 1 ou 2: ").strip()
    if escolha == '1':
        main_console()
    elif escolha == '2':
        iniciar_interface()
    else:
        print("Opção inválida.")
        escolher_interface()

def main_console():
    simular = True
    while simular:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("[SIMULADOR DE RELAÇÕES DE MERCADO]")

        print_pessoas(pessoas)
        print_empresas(empresas)

        resposta = input("\nDigite um número para avançar N meses, 'enter' para avançar 1 mês ou 'sair' para encerrar: ").strip().lower()

        if resposta.isdigit():
            meses = int(resposta)
            for _ in range(meses):
                simular_mercado(pessoas, empresas, categorias, percentuais)
        elif resposta == "":
            simular_mercado(pessoas, empresas, categorias, percentuais)
        elif resposta == "sair":
            simular = False

if __name__ == "__main__":
    escolher_interface()