x = 10
type(x)
largura_retangulo = float(input("Digite a largura do retangulo:"))
comprimento_retangulo = float(input("Digite o comprimento do retangulo:"))
area_retangulo = largura_retangulo * comprimento_retangulo
raio = float(input("Digite o raio do círculo:"))
area_circulo = 3,14 * (raio * raio)
area_total = area_retangulo - area_circulo
print(f"A área total é: {area_total}")