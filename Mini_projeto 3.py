import time
roxo = '\033[35m'
azul = '\033[34m'
verde = '\033[32m'
italico = '\033[3m'
reset = '\033[0m'
ipca = float("5.53")
cdi = float("14.65")
poupança = float("6.00")
print("SIMULADOR DE INVESTIMENTOS")
time.sleep(1.0)
print(f"{italico}Olá, vou te ajudar a simular as oportunidades de investimentos!{reset}")
time.sleep(1.5)
print()
print(f"Pra começar, quero te dizer que as {azul}taxas anuais{reset} que estou utilizando são:")
time.sleep(1.5)
print(f"{azul}IPCA{reset} (inflação): {roxo}{ipca}%{reset}")
time.sleep(1.0)
print(f"{azul}CDI{reset} (juros):.... {roxo}{cdi}%{reset}")
time.sleep(1.0)
print(f"{azul}Poupança{reset}:....... {roxo}{poupança:.2f}%{reset}")
time.sleep(3.0)
valor_investimento = float(input(f"Agora me informa o valor em reais que você quer investir: {verde}R$ "))
time.sleep(1.0)
print(f"{reset}{italico}Ok, registrei o valor do seu investimento.{reset}")
time.sleep(3.0)
print()
cdb1 = cdi * 1.00
cdb2 = cdi * 1.10
cdb3 = cdi * 1.20
lca = cdi * 0.95
print("Essas são as opções de investimentos que estão disponíveis para você:")
time.sleep(1.5)
print(f"[A] {azul}CDB{reset} valendo 100% do CDI, taxa final de {roxo}{cdb1:.2f}%{reset}")
time.sleep(1.0)
print(f"[B] {azul}CDB{reset} valendo 110% do CDI, taxa final de {roxo}{cdb2:.2f}%{reset}")
time.sleep(1.0)
print(f"[C] {azul}CDB{reset} valendo 120% do CDI, taxa final de {roxo}{cdb3:.2f}%{reset}")
time.sleep(1.0)
print(f"[D] {azul}LCA{reset} valendo  95% do CDI, taxa final de {roxo}{lca:.2f}%{reset}")
time.sleep(1.0)
print(f"{italico}Obs.: Lembre que o CDB retém o IR na fonte, enquanto o LCA não.{reset}")
time.sleep(1.5)
print()
tipo_investimento = input("Qual investimento você quer fazer? (A, B, C ou D): ").upper().strip()
time.sleep(1.0)
print(f"{italico}Ok, registrei a sua opção de investimento.{reset}")
time.sleep(1.5)
if tipo_investimento.upper() in ["A","B","C"]:
    print(f"{italico}Como você escolheu CDB, vou te lembrar as taxas regressivas de IR:{reset}")
    time.sleep(1.0)
    print(f"{italico}Até 6 meses:...... {roxo}22.50%{reset}")
    time.sleep(1.0)
    print(f"{italico}Até 12 meses:..... {roxo}20.00%{reset}")
    time.sleep(1.0)
    print(f"{italico}Até 24 meses:..... {roxo}17.50%{reset}")
    time.sleep(1.0)
    print(f"{italico}Acima de 24 meses: {roxo}15.00%{reset}")
    time.sleep(1.5)
#PARTE 2
ir1 = 22.50
ir2 = 20.00
ir3 = 17.50
ir4 = 15.00 
tempo_investimento = int(input(f"Quanto tempo você gostaria de esperar para resgatar esse investimento? (em meses) {azul}"))
time.sleep(1.0)
if tempo_investimento <= 6: 
    ir_aplicado =  ir1
elif tempo_investimento <= 12:
    ir_aplicado = ir2
elif tempo_investimento <= 24:
    ir_aplicado = ir3
else:
    ir_aplicado = ir4
print(f"{reset}{italico}Ok, registrei o tempo para o resgate.{reset}")
time.sleep(1.0)
print()
print("TAXAS UTILIZADAS")
time.sleep(1.0)
print(f"- Taxa de IR aplicada...... {roxo}{ir_aplicado:.2f}%{reset}")
time.sleep(1.0)
if tipo_investimento == "A":
    rendimento_anual = cdb1
elif tipo_investimento == "B":
    rendimento_anual = cdb2
elif tipo_investimento == "C":
    rendimento_anual = cdb3
elif tipo_investimento == "D":
    rendimento_anual = lca
print(f"- Taxa de rendimento anual. {roxo}{rendimento_anual:.2f}%{reset}")
time.sleep(1.0)
if tipo_investimento == "A":
    rendimento_mensal = ((1+rendimento_anual/100)**(1/12)-1)*100
elif tipo_investimento == "B":
    rendimento_mensal = ((1+rendimento_anual/100)**(1/12)-1)*100
elif tipo_investimento == "C":
    rendimento_mensal = ((1 + rendimento_anual/100)**(1/12)-1)*100
elif tipo_investimento == "D":
    rendimento_mensal = ((1+rendimento_anual/100)**(1/12)-1)*100
print(f"- Taxa de rendimento mensal {roxo}{rendimento_mensal:.2f}%{reset}")
time.sleep(1.0)
print()
print("RESULTADO:")
time.sleep(1.5)
print(f"Valor investido:...... {verde}R$ {valor_investimento:.2f}{reset}")
time.sleep(1.0)
print(f"Rendendo pelo tempo de {azul}{tempo_investimento} meses{reset}")
time.sleep(1.0)
print(f"Dedução do IR de...... {roxo}{ir_aplicado:.2f}%{reset}")
time.sleep(1.0) 
valor_bruto = float(valor_investimento * (1 + rendimento_mensal / 100) ** tempo_investimento)
lucro_bruto = float((valor_bruto - valor_investimento))
if tipo_investimento == "D":
    valor_liquido = valor_bruto
    valor_deduzido = 0
else:
    valor_deduzido = lucro_bruto * (ir_aplicado/100)
    valor_liquido = float(valor_bruto - valor_deduzido)
lucro_total = float(valor_liquido - valor_investimento)
print(f"Valor deduzido é de:.. {verde}R$ {valor_deduzido:.2f}{reset}")
time.sleep(1.0)
print(f"O resgate será de:.... {verde}R$ {valor_liquido:.2f}{reset}")
time.sleep(1.0)
print(f"O lucro total será de. {verde}R$ {lucro_total:.2f}{reset}")
time.sleep(3.0)
#PARTE 3
analises_adicionais = input(f"{italico}Você gostaria de ver algumas análises adicionais (sim/não)?{reset}").strip().lower()
time.sleep(1.0)
print()
valor_poupanca = valor_investimento * (1 + poupança / 100 / 12)**tempo_investimento
lucro_poupanca = valor_poupanca - valor_investimento
diferenca_lucros = lucro_total - lucro_poupanca
ipca_anual = 1.0553
ipca_mensal = 1.00460833
ipca_acumulado = ipca_mensal ** tempo_investimento
inflacao_acumulada = ipca_acumulado
inflacao_percentual = inflacao_acumulada * 100
desvalorizacao = (1 / ipca_acumulado)
desvalorizacao_percentual = desvalorizacao * 100
valor_corrigido = valor_investimento * ipca_acumulado
resgate_proporcional = valor_liquido / ipca_acumulado
poupanca_proporcional = valor_poupanca / ipca_acumulado
if analises_adicionais == "sim":
    print("ANÁLISES POUPANÇA")
    print(f"Se você tivesse investido {verde}R${valor_investimento:.2f}{reset}")
    time.sleep(1.0)
    print(f"Na poupança, ao final dos {azul}{tempo_investimento} meses{reset}")
    time.sleep(1.0)
    print(f"O valor resgatado seria.. {verde}R$ {valor_poupanca:.2f}{reset}")
    time.sleep(1.0)
    print(f"E o lucro total.......... {verde}R$ {lucro_poupanca:.2f}{reset}")
    time.sleep(1.0)
    print(f"A diferença de lucro é de {verde}R$ {diferenca_lucros:.2f}{reset}")
    time.sleep(1.0)
    print()
    print("ANÁLISE INFLAÇÃO")
    time.sleep(1.0)
    print(f"A inflação acumulada foi de........................ {roxo}{inflacao_percentual:.2f}%{reset}")
    time.sleep(1.0)
    print(f"resultando em uma desvalorização de................ {roxo}{desvalorizacao_percentual:.2f}%{reset}")
    time.sleep(1.0)
    print(f"Por exemplo, se você comprava algo por............. {verde}R$ {valor_investimento:.2f}{reset}")
    time.sleep(1.0)
    print(f"O mesmo item custaria, corrigido pela inflação..... {verde}R$ {valor_corrigido:.2f}{reset}")
    time.sleep(1.0)
    print(f"O resgate proporcionalmente ao valor corrigido fica {verde}R$ {resgate_proporcional:.2f}{reset}")
    time.sleep(1.0)
    print(f"Já na poupança o proporcional a essa correção seria {verde}R$ {poupanca_proporcional:.2f}{reset}")
    time.sleep(3.0)
    print()
    print("RESUMO")
    time.sleep(1.0)
    print(f"Valor investido:..... {verde}R$ {valor_investimento:.2f}{reset}")
    time.sleep(1.0)
    print(f"Valor resgatado:..... {verde}R$ {valor_liquido:.2f}{reset}")
    time.sleep(1.0)
    print(f"Se fosse na poupança: {verde}R$ {valor_poupanca:.2f}{reset}")
    time.sleep(1.0)
    print(f"Correção da inflação: {verde}R$ {valor_corrigido:.2f}{reset}")
    time.sleep(1.0)
    print()
    print(f"{italico}Espero ter ajudado!{reset}")
else:
    print("RESUMO")
    time.sleep(1.0)
    print(f"Valor investido:..... {verde}R$ {valor_investimento:.2f}{reset}")
    time.sleep(1.0)
    print(f"Valor resgatado:..... {verde}R$ {valor_liquido:.2f}{reset}")
    time.sleep(1.0)
    print(f"Se fosse na poupança: {verde}R$ {valor_poupanca:.2f}{reset}")
    time.sleep(1.0)
    print(f"Correção da inflação: {verde}R$ {valor_corrigido:.2f}{reset}")
    time.sleep(3.0)
    print()
    print(f"{italico}Espero ter ajudado!{reset}")