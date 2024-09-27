x = 10
type(x)
preco_original = float(input("Digite o preço original do produto:"))
valor_imposto = float(input("Digite o valor do imposto(%):"))
desconto = float(input("Digite o valor do desconto(%):"))
preco_com_imposto = preco_original + (preco_original * (valor_imposto/100))
preco_final = preco_com_imposto - (preco_com_imposto * (desconto/100))
print(f"O preço final do produto é: {preco_com_imposto}")
