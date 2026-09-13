# Entrada de informações
valor_compra = float(input("Digite o valor de sua compra em Reais:")) #Aqui pede o valor gasto pelo cliente sem o desconto

# Processamento de informações
if valor_compra < 200: #Aqui está falando que se o valor for menor que 200 o desconto será de 5%
    valor_final5 = valor_compra * 0.95
elif valor_compra >= 200 and valor_compra < 300: #Aqui está falando que se o valor for maior que 200 e menor que 300 o desconto será de 10%
    valor_final10 = valor_compra * 0.90
elif valor_compra >=300: #Aqui está falando que se o valor for maior que 300 o desconto será de 15%
    valor_final15 = valor_compra * 0.85

# Saida de informações
if valor_compra < 200:
    print(f"O seu valor de compra é {valor_compra} e o valor final com desconto será de R${valor_final5:.2f}") #Aqui está o resultado após o desconto aplicado de 5%
elif valor_compra >= 200 and valor_compra < 300:
    print(f"O seu valor de compra é {valor_compra} e o valor final com desconto será de R${valor_final10:.2f}") #Aqui está o resultado após o desconto aplicado de 10%
elif valor_compra >=300:
    print(f"O seu valor de compra é {valor_compra} e o valor final com desconto será de R${valor_final15:.2f}") #Aqui está o resultado após o desconto aplicado de 15%