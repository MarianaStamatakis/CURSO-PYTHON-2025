#%%
# Faça um programa que dê bom dia;

print("Bom dia!")

#%%
#faça um programa que de bom dia, peregunta o nome da pessoa e responde que é um prazer conhece-la, citando o nome.

nome = input("Bom dia! Qual o seu nome?")
print("Prazer em te conhecer",nome)

#%%
#Crie uma história simples. Adicione essa história em um programa. A cada parágrafo, a história deve aguardar o usuário apertar enter para dar continuidade.

p1 = "Era uma vez, em um reino distante, um jovem aventureiro chamado Leo."
p2 = "Leo sonhava em encontrar um tesouro escondido nas profundezas da floresta encantada."
p3 = "Um dia, ele decidiu partir em sua jornada, enfrentando desafios e fazendo novos amigos pelo caminho."
p4 = "Após muitas aventuras, Leo finalmente encontrou o tesouro e voltou para casa como um herói. Fim."

input(p1)
input(p2)
input(p3)   
input(p4)



#%%
#Faça um programa que receba um número inteiro e calcule sua raiz quadrada e exiba o resultado.

numero = input("Digite um número inteiro")
numero = int(numero)

resultado = numero ** 0.5
resultado = round(resultado, 2)

print("A raiz quadrada de", numero, "é", resultado)


#%%
#Faça um programa que exiba o dobro de um número insirido pelo ususário.

numero = input("Digite um número inteiro")
numero = int(numero)

resultado = numero *2

print("O dobro de", numero, "é", resultado)
# %%
