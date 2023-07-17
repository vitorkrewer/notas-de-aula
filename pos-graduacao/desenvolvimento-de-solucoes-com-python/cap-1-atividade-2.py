# Disciplina - Desenvolvimento de Soluções com Python
# Capítulo 1 - Fundamentos de Lógica da Programação
# Atividade 02 - Crie um programa que solicite ao usuário o tamanho da base e a altura de um triângulo e calcule a sua área
# Fórmula - b.a/2 onde b = base e a = altura

print("Seja bem-vindo a calculadora da área de um triângulo. Informe os dados corretamente.")
base_triangulo = input("Informe a base do triângulo: ")
base_triangulo = base_triangulo.replace(",", ".")
base_triangulo_convert = float(base_triangulo)

altura_triangulo = input("Informe a altura do triângulo: ")
altura_triangulo = altura_triangulo.replace(",", ".")
altura_triangulo_convert = float(altura_triangulo)

area_triangulo = (base_triangulo_convert*altura_triangulo_convert)/2
print("O triângulo tem ", area_triangulo, "de área total")

# Utilizado a variável do tipo float para entrada dos dados. É necessário utilizar pontos para números decimais. Para facilitar a usabilidade, acrescentei a conversão de dados, dando liberdade ao usuário para utilizar ponto ou vírgula ao inserir os dados

# É aceito tanto ponto como vírgula em qualquer dos inputs. Se o usuário utilizar vírgula no primeiro input e ponto no segundo input, não irá alterar o resultado ou ocorrer ValueError: could not convert string to float, por exemplo

'''
Script utilizando dados do tipo int
print("Seja bem-vindo a calculadora de área de triângulos. Informe os dados corretamente.")
base_triangulo = int(input("Informe a base do triângulo: "))
altura_triangulo = int(input("Informe a altura do triângulo: "))
area_triangulo = (base_triangulo*altura_triangulo)/2
print("O triângulo tem ", area_triangulo, "de área total")
'''

'''
Script utilizando dados do tipo float
print("Seja bem-vindo a calculadora de área de triângulos. Informe os dados corretamente.")
base_triangulo = float(input("Informe a base do triângulo: "))
altura_triangulo = float(input("Informe a altura do triângulo: "))
area_triangulo = (base_triangulo*altura_triangulo)/2
print("O triângulo tem ", area_triangulo, "de área total")
'''