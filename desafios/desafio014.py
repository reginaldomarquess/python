# Escreva uma programa que converta uma temperatura digitada em °C e converta para °F.

temperatura_celsius = (float(input("Digite a temperatura em °C: ")))
# Aqui foi aplicada a ordem de precedência das operações matemáticas, primeiro a multiplicação e divisão, depois a soma.
temperatura_f = temperatura_celsius * 9 / 5 + 32

print(
    f"A temperatura {temperatura_celsius}°C convertida para Fahrenheit é {temperatura_f:.1f}°F")
