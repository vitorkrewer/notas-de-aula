# Disciplina - Desenvolvimento de Soluções com Python
# Capítulo 1 - Fundamentos de Lógica da Programação
# Atividade 01 - Crie um programa que receba o ano de nascimento do usuário e calcule qual idade ele terá em 2035.


print("Olá! Informe corretamente seus dados para saber quantos anos terá na data futura informada. Vamos lá?")
data_nasc = int(input("Qual é a data do seu nascimento? "))
print('Entendi. Na data de hoje você tem', data_nasc, 'anos de idade.')
ano_atual = int(input("Agora, informe em que ano você está vivendo? "))
print(ano_atual)
ano_futuro = int(input("Em qual data futura você deseja saber sua idade? "))
print(ano_futuro)
print("Dados computados. Atualmente você está com ", ano_atual - data_nasc, "anos de idade.")
idade = int(ano_atual - data_nasc)
idade_futura = idade + (ano_futuro - ano_atual)
print("No ano de ", ano_futuro, "você terá ", idade_futura, "anos de idade!")

# Alterei a variável relativa a entrada da data de 2035 para dar liberdade ao usuário para inserir a data que desejar