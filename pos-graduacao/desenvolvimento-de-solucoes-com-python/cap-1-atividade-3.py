
# Disciplina - Desenvolvimento de Soluções com Python
# Capítulo 1 - Fundamentos de Lógica da Programação
# Atividade 03 - Crie um programa que solicite a massa e a altura do usuário e calcule seu IMC.
# A fórmula matemática é IMC = Peso / (Altura x Altura)

print("Calculadora do IMC - Índice de Massa Corporal. Insira seus dados corretamente.")
peso = float(input("Qual é o seu peso? "))
altura = float(input("Qual é a sua altura? "))
imc = peso/(altura*altura)
print("SeU IMC é de ", imc, "kg/m2")

if imc <= 25:
    print("Você está dentro do peso ideal.")
elif imc >= 25 and imc <= 30:
    print("Você está acima do peso.")
elif imc >= 30 and imc <= 35:
    print("Você está acima do peso. Faixa de Obsesidade I.")
elif imc >=35 and imc <= 40:
    print("Você está acima do peso. Faixa de Obsesidade II.")
elif imc >=40:
    print("Você está acima do peso. Faixa de Obsesidade Mórbida.")
else:
    print("kg/m2 acima de 25 é um indicativo de que você está acima do peso.")

# Neste capítulo do livro ainda não foi ministrado conteúdo relativo a lógica booleana e estruturas de condição if, elif e else. Optei por incluir para com a ideia de dar feedback ao usuário. Acima de 25 kg/m2 é considerado Acima do Peso

'''
RESULTADO	SITUAÇÃO
Abaixo de 17	Muito abaixo do peso
Entre 17 e 18,49	Abaixo do peso
Entre 18,5 e 24,99	Peso normal
Entre 25 e 29,99	Acima do peso
Entre 30 e 34,99	Obesidade I
Entre 35 e 39,99	Obesidade II (severa)
Acima de 40	Obesidade III (mórbida)

'''