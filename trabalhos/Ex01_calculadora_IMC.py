peso = float(input("Digite seu Peso"))
altura = float(input("Digite sua Altura"))

imc = (peso/altura**2)
print(imc)

if peso<=0 and altura<=0:
    print("Digite algo valido")

if imc<=18.5:
    print("Abaixo do peso")

elif imc>=18.5 and imc<=24.9:
    print("Peso normal")
elif imc>=25 and imc<=29.9:
    print("Sobrepeso")
elif imc>=30 and imc<=34.9: 
    peso_perdido=peso*0.2
    print("Obesidade grau I",peso_perdido)
elif imc>=35 and imc<=39.9: 
    peso_perdido=peso*0.3
    print("Obesidade grau II",peso_perdido)
else:
    peso_perdido=peso*0.4
    print("Obesidade grau III",peso_perdido)
