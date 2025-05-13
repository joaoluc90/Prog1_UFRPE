nome_completo = "Joao Lucas Cosme"
dia_nascimento = 16
mes_nascimento = 5
ano_nascimento = 1998
print(f"{nome_completo}, nascido em {dia_nascimento}/{mes_nascimento}/{ano_nascimento}")
anos = 2025 - ano_nascimento
meses = 5 - mes_nascimento
dias = 14 - dia_nascimento
anos_total = anos * 365
meses_total = meses * 30
dias_total = anos_total + meses_total + dias
print(f"{nome_completo} tem {dias_total} dias de vida")
idade = int(dias_total / 365)
print(f"{nome_completo} tem {idade} anos de vida")
print()
print()
print(f"----")
print()
print()
#parte2
patrimonio = float(2000)
salario = float(1518)
gastos = float(1077)
investimentos_mensal = float(150)
print(f"{nome_completo} recebe mensalmente R${salario}")
equivalencia_salario = float(salario / 1518)
print(f"Os recebimentos equivalem a {equivalencia_salario} salários mínimos")
print(f"{nome_completo} tem um patrimônio de R${patrimonio}")
print(f"{nome_completo} gasta R${gastos} por mês")
equivalencia_gastos = gastos / salario * 100
print(f"Os gastos equivalem a {equivalencia_gastos:.2f}% da sua renda")
print(f"{nome_completo} investe mensalmente R${investimentos_mensal}")
renda_investimentos = patrimonio * 0.5 / 100
patrimonio_resultante = renda_investimentos + patrimonio + investimentos_mensal
print(f"{nome_completo} Após 1 mês, está com o patrimônio de R${patrimonio_resultante}")
dinheiro_livre = (salario) - gastos - investimentos_mensal
print(f"O saldo de dinheiro livre no mês foi de R${dinheiro_livre}")
print()
print()
print(f"----")
print()
print()
#parte3
patrimonio_anual = patrimonio * (1 + 0.005)**12
rendimento_anual = patrimonio_anual - patrimonio
print(f"Se {nome_completo} não investir nada, após 12 meses o seu patrimônio terá rendido R${rendimento_anual:.2f} e será R${patrimonio_anual:.2f}")