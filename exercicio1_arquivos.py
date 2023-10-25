import random

produtos = [
    ['Celular', 'Samsung', 3270],
    ['Celular', 'Apple', 5865],
    ['Smart TV', 'Samsung', 4270.99],
    ['Smart TV', 'LG', 3899.99],
    ['Notebook', 'Dell', 4269.99],
    ['Notebook', 'Acer', 3800],
    ['Geladeira', 'Brastemp', 6599],
    ['Geladeira', 'Samsung', 8540],
    ['Máquina de lavar', 'Brastemp', 3800],
    ['Máquina de lavar', 'LG', 5000]
]

lojas = ["Ibirapuera", 'Centro', 'Lapa']

with open('faturamento_anual.txt', 'w') as arq:
    for x in range(100000):
        i = random.randint(0, len(produtos) - 1)
        prod = produtos[i]
        i = random.randint(0, len(lojas) - 1)
        loja = lojas[i]
        dia = random.randint(1, 31)
        mes = random.randint(1, 12)
        if mes == 2 and dia > 28:
            dia = 28
        elif dia == 31 and mes in (4, 6, 9, 11):
            dia = 30            


        qtd = random.randint(1, 20)
        arq.write(f"{prod[0]};{prod[1]};{loja};2022-{mes}-{dia};{qtd};{prod[2]}\n")
        
print("Arquivo de faturamento gerado com sucesso!")