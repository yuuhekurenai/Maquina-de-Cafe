import opcoes

bolsa = 0

def transacao_feita(dinheiro_recebido, valor_item):
    """retorna verdadeiro se o pagamento for aceito , e falso se o valor é insuficiente"""

    global bolsa # Global retorna a variavel que está fora da função.
    if dinheiro_recebido >= valor_item:
        troco = round(dinheiro_recebido - valor_item, 2)
        print(f"Aqui está seu troco {troco}")
        bolsa += dinheiro_recebido
        return True

def recursos_suficientes(pedido):
    """# Retorna verdadeiro de o pedido por ser feito,
    # E retorna falso se não haver ingredientes suficientes."""
    suficiente = True
    for item in pedido:
        if pedido(item) >= opcoes.MENU[item]:
            print(f"Desculpe mas não há {item}")
            suficiente = False
        return suficiente

def processo_valor():
    """ retorna o o valor total"""
    print("Insira o valor do pedido")
    total = input("Quantos reais ?")
    total += input("Quantos centavos ?")
    return total


maquina_on = True
""" enquanto a maquina estiver ligada
# Irá informar as opçoes para o comprador"""
while maquina_on:
    escolha = input("Qual opção você deseja? (espresso , latte ou cappuccino? ").lower()
    if escolha == "off":
        maquina_on = False
    elif escolha == "menu":
        print(f"Agua:{opcoes.recursos['agua']}")
        print(f"Leite:{opcoes.recursos['leite']}")
        print(f"Café:{opcoes.recursos['cafe']}")
        print(f"lucro: {bolsa}")
    else:
        bebida = opcoes.MENU[escolha]
    print(bebida)
    if recursos_suficientes(bebida['ingredients']):
        pagamento = processo_valor()
        transacao_feita(pagamento, bebida[opcoes.MENU['cost']])
