#%%

produto = input("escolha a sua garrafa de água: Digite 1 para água mineral natural ou 2 para água mineral com gás.")
produto = int(produto)  

if produto == 1:
    print("Água mineral natural R$1,50")

elif produto == 2:
    print("Água mineral com gás R$2,50")
 
else:
    print("Produto inválido. Por favor, escolha 1 ou 2.")
# %%
produto = input("escolha a sua garrafa de água: Digite 1 para água mineral natural ou 2 para água mineral com gás.")
produto = int(produto)  
quantidade = input("Insira o número de garrafas que você irá querer:")
quantidade = int(quantidade)  
texto_conta = "Valor total do pedido: R$"

if produto == 1:
    print( "Pedido:",quantidade,"unid de Água mineral natural R$1.50.")
    print(texto_conta, quantidade * 1.5)

elif produto == 2:
    print( "Pedido:",quantidade,"unid de Água mineral com gás R$2.50.")
    print(texto_conta, quantidade * 2.5)
    
else:
    print("Produto inválido. Por favor, escolha 1 ou 2.")

# %%
produto = input("Escolha o tamanho do seu sorvete: Digite 1 para casquinha, 2 para cascão e 3 para cestinha.")
produto = int(produto)  
sabor = input("Escolha o sabor do sorvete: Chocolate, Creme ou Morango.")
sabor = str.lower(sabor)
cobertura = input("Digite o numero da cobertura desejada: 1 para Caramelo,2 para Morango, 3 para Chocolate ou 0 para sem cobertura")
cobertura = int(cobertura)

if produto == 1 and cobertura == 1:
    produto = "casquinha"
    valor_produto = 1.0
    cobertura = "caramelo"
    valor_cobertura = 1.5

    print( "Pedido:",produto,"de",sabor,"com cobertura de",cobertura,"R$",valor_produto + valor_cobertura)
    
elif produto == 1 and cobertura == 2:
    produto = "casquinha"
    valor_produto = 1.0
    cobertura = "morango"
    valor_cobertura = 1.5

    print( "Pedido:",produto,"de",sabor,"com cobertura de",cobertura,"R$",valor_produto + valor_cobertura)
    
elif produto == 1 and cobertura == 3:
    produto = "casquinha"
    valor_produto = 1.0
    cobertura = "chocolate"
    valor_cobertura = 1.5

    print( "Pedido:",produto,"de",sabor,"com cobertura de",cobertura,"R$",valor_produto + valor_cobertura)

elif produto == 1 and cobertura == 0:
    produto = "casquinha"
    valor_produto = 1.0
    cobertura = "sem cobertura"
    valor_cobertura = 0

    print( "Pedido:",produto,"de",sabor,"com cobertura de",cobertura,"R$",valor_produto + valor_cobertura)

elif produto == 2 and cobertura == 1:
    produto = "cascão"
    valor_produto = 2.5
    cobertura = "caramelo"
    valor_cobertura = 1.5

    print( "Pedido:",produto,"de",sabor,"com cobertura de",cobertura,"R$",valor_produto + valor_cobertura)
    
elif produto == 2 and cobertura == 2:
    produto = "cascão"
    valor_produto = 2.5
    cobertura = "morango"
    valor_cobertura = 1.5

    print( "Pedido:",produto,"de",sabor,"com cobertura de",cobertura,"R$",valor_produto + valor_cobertura)
    
elif produto == 2 and cobertura == 3:
    produto = "cascão"
    valor_produto = 2.5
    cobertura = "chocolate"
    valor_cobertura = 1.5

    print( "Pedido:",produto,"de",sabor,"com cobertura de",cobertura,"R$",valor_produto + valor_cobertura)

elif produto == 2 and cobertura == 0:
    produto = "cascão"
    valor_produto = 2.5
    cobertura = "sem cobertura"
    valor_cobertura = 0

    print( "Pedido:",produto,"de",sabor,"com cobertura de",cobertura,"R$",valor_produto + valor_cobertura)

elif produto == 3 and cobertura == 1:
    produto = "cestinha"
    valor_produto = 4.0
    cobertura = "caramelo"
    valor_cobertura = 1.5

    print( "Pedido:",produto,"de",sabor,"com cobertura de",cobertura,"R$",valor_produto + valor_cobertura)
    
elif produto == 3 and cobertura == 2:
    produto = "cestinha"
    valor_produto = 4.0
    cobertura = "morango"
    valor_cobertura = 1.5

    print( "Pedido:",produto,"de",sabor,"com cobertura de",cobertura,"R$",valor_produto + valor_cobertura)
    
elif produto == 3 and cobertura == 3:
    produto = "cestinha"
    valor_produto = 4.0
    cobertura = "chocolate"
    valor_cobertura = 1.5

    print( "Pedido:",produto,"de",sabor,"com cobertura de",cobertura,"R$",valor_produto + valor_cobertura)

elif produto == 3 and cobertura == 0:
    produto = "cestinha"
    valor_produto = 4.0
    cobertura = "sem cobertura"
    valor_cobertura = 0

    print( "Pedido:",produto,"de",sabor,"com cobertura de",cobertura,"R$",valor_produto + valor_cobertura)


else:
    print("Produto inválido. Por favor verifique as opções e escolha novamente")

# %%
