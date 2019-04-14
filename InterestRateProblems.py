# PROBLEMA 1
# Informações do problema 1
valor_mensal = 129.99
valor_a_vista = 1208.91


# Somatório da série de pagamentos uniformes (10 parcelas)
def f1(x, r, v):
    return (r * ((x ** 9) + (x ** 8) + (x ** 7) + (x ** 6) + (x ** 5) + (x ** 4) + (x ** 3) + (x ** 2) + x + 1)) - (
                v * x ** 9)


# Derivada da soma da série de pagamentos uniformes
def df1(x, r, v):
    return r * ((9 * x ** 8) + (8 * x ** 7) + (7 * x ** 6) + (6 * x ** 5) + (5 * x ** 4)
                + (4 * x ** 3) + (3 * x ** 2) + (2 * x) + 1) - (9 * v * (x ** 8))


# Função - Newton-Raphson - Encontrar zero de função
# Entradas: função de interesse, a sua derivada e o chute inicial x0
# Saída: raíz da função
def newton_raphson(x, f, df):
    h = f(x, valor_mensal, valor_a_vista) / df(x, valor_mensal, valor_a_vista)
    while abs(h) >= 0.0001:  # limitante do erro
        h = f(x, valor_mensal, valor_a_vista) / df(x, valor_mensal, valor_a_vista)
        # x(i+1) = x(i) - f(x)/f'(x)
        x = x - h

    # print("valor da raíz: ", "%.4f" % x)

    return x


# valor inicial do método Newton-Raphson
x0 = 2
# cálculo da taxa de juros mensal
taxaM = newton_raphson(x0, f1, df1) - 1  # o fator de acumulação é x = 1 + (taxaM/100)
# cálculo da taxa de juros anual
taxaA = 100 * ((1 + taxaM) ** 12 - 1)

print("-----------------SOLUÇÃO DO PROBLEMA 1---------------")
print("TAXA DE JUROS MENSAL(%):", "%.4f" % (taxaM * 100))
print("TAXA DE JUROS ANUAL(%):", "%.4f" % taxaA)

# PROBLEMA 2
# Informações do problema 2
valor_a_vista = 129000
valor_mensal = [27000.00, 24000.00, 30000.00, 32000.00, 22000.00]  # vetor de 5 posições


def f2(x, r, v):
    return (r[0] * x ** 4) + (r[1] * x ** 3) + (r[2] * x ** 2) + (r[3] * x) + r[4] - (v * x ** 4)


def df2(x, r, v):
    return (4 * r[0] * x ** 3) + (3 * r[1] * x ** 2) + (2 * r[2] * x) + r[3] - (4 * v * x ** 3)


# valor inicial do método Newton-Raphson
x0 = 2
# Taxa de Juros mensal
taxaM = newton_raphson(x0, f2, df2) - 1  # o fator de acumulação é x = 1 + (taxaM/100)

print("\n")
print("-----------------SOLUÇÃO DO PROBLEMA 2---------------")
print("TAXA DE JUROS MENSAL(%):", "%.4f" % (taxaM * 100))
print("Como a taxa de juros da opção 2 (parcelar compra) é", "%.4f" % (taxaM * 100),
      "% e a taxa do empréstimo de 2%, é vantajoso fazer o empréstimo")


#Problema 3
#Informações do problema 3

valor_a_vista = 889.18 #valor do título
valor_mensal = 48.81 #valor referente ao valor semestral, mantido o nome da variável por conta da função newton-raphson

def f3(x,r,v):
    return r*((x ** 120) + (x ** 114) + (x ** 108) + (x ** 102) + (x ** 96) + (x ** 90) + (x ** 84) + (x ** 78) + (x ** 72)
              + (x ** 66) + (x ** 60) + (x ** 54) + (x ** 48) + (x ** 42) + (x ** 36) + (x ** 30) + (x ** 24) + (x ** 18)
              + (x ** 12) + (x ** 6) + (1000+r) - (v*x ** 120))

def df3(x,r,v):
    return r*((120 * x ** 119) + (114 * x ** 113) + (108 * x ** 107) + (102 * x ** 101) + (96 * x ** 95) + (90 * x ** 89) +
              (84 * x ** 83) + (78 * x ** 77) + (72 * x ** 71) + (66 * x ** 65) + (60 * x ** 59) + (54 * x ** 53) +
              (48 * x ** 47) + (42 * x ** 41) + (36 * x ** 35) + (30 * x ** 29) + (24 * x ** 23) + (18 * x ** 17) +
              (12 * x ** 11) + (6 * x ** 5) + (120 * v * x * 119))


# valor inicial do método Newton-Raphson
x0 = 2
# cálculo da taxa de juros mensal
taxaM = newton_raphson(x0, f3, df3) - 1  # o fator de acumulação é x = 1 + (taxaM/100)
# cálculo da taxa de juros anual
taxaA = 100 * ((1 + taxaM) ** 12 - 1)

print("\n")
print("-----------------SOLUÇÃO DO PROBLEMA 3---------------")
print("TAXA DE JUROS MENSAL(%):", "%.4f" % (taxaM * 100))
print("TAXA DE JUROS ANUAL(%):", "%.4f" % taxaA)