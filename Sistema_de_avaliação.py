quantidade_excelente = 0
quantidade_ruim = 0

for i in range(50):
    print("Entrevistado", i + 1)
    nome_do_cliente = str(input("Digite o seu nome: "))
    idade = float(input("Digite a sua idade: "))
    Avaliacao = float(input("Excelente = 1, Bom = 2, Ruim = 3 "))
    if Avaliacao == 1:
        quantidade_excelente += 1
    elif Avaliacao == 3:
        quantidade_ruim += 1  


  

print("\nResultado da pesquisa:")
print("Quantidade de respostas excelentes:", quantidade_excelente)
print("Quantidade de respostas ruins:", quantidade_ruim)