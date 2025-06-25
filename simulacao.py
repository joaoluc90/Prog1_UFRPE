def simulando_pessoa(pessoa, empresas, categorias, percentuais):

    pessoa.conforto = 0
    pessoa.rendimento_mes = pessoa.salario + pessoa.patrimonio * 0.05
    gasto_mensal = 0

    # passa pelas 5 categorias (moradia, alimentação …) ─
    for i, categoria in enumerate(categorias):

        orcamento = pessoa.rendimento_mes * percentuais[i]

        # empresas disponíveis, com oferta > 0
        opcoes = [e for e in empresas if e.categoria == categoria and e.oferta > 0]
        if not opcoes:
            continue  # ninguém vendeu nada nessa categoria

        # tenta comprar o produto de maior qualidade DENTRO do orçamento mensal
        candidatos = [e for e in opcoes if e.o_preco() <= orcamento]

        compra = None
        pagou_com_patrimonio = False

        if candidatos:
            # escolhe o de maior qualidade
            compra = max(candidatos, key=lambda e: e.qualidade)
        else:
            # não cabia no orçamento mensal → usa patrimônio p/ o + barato
            mais_barato = min(opcoes, key=lambda e: e.o_preco())
            if pessoa.patrimonio >= mais_barato.o_preco():
                compra = mais_barato
                pagou_com_patrimonio = True

        
        if compra:
            preco = compra.o_preco()

            if pagou_com_patrimonio:
                pessoa.patrimonio -= preco
            else:
                gasto_mensal += preco

            # conforto cresce com a qualidade do produto
            pessoa.conforto += compra.qualidade

            # atualiza empresa
            compra.oferta -= 1
            compra.vendas += 1
            compra.lucro_total += preco - compra.custo

    
    poupanca = pessoa.rendimento_mes - gasto_mensal
    pessoa.patrimonio += poupanca


def ajustar_empresa(empresa):
    # vendeu tudo
    if empresa.oferta == 0:
        empresa.reposicao += 1
        empresa.margem += 0.01

    # sobrou muito estoque
    elif empresa.oferta >= 10:
        empresa.reposicao = max(1, empresa.reposicao - 1)
        empresa.margem = max(0, empresa.margem - 0.01)   # margem nunca negativa


def simular_mercado(pessoas, empresas, categorias, percentuais):

    
    for e in empresas:
        e.oferta += e.reposicao          # repõe
        e.vendas = 0                     # zera vendas do mês

    for p in pessoas:
        simulando_pessoa(p, empresas, categorias, percentuais)

    for e in empresas:
        ajustar_empresa(e)