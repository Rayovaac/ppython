peso = float(input("Digite seu Peso"))
altura = float(input("Digite sua Altura"))

imc = (peso/altura**2)
print(imc)

if peso<=0 and altura<=0:
    print("O numero e negativo Por favor Digite Algo valido Arrombado")

if imc<=18.5:
    print("Vai se alimentar Tu Vai morrer")

elif imc>=18.5 and imc<=24.9:
    print("Boa Ta Na media")
elif imc>=25 and imc<=29.9:
    print("Ta quase thais Carla")
elif imc>=30 and imc<=34.9: 
    peso_perdido=peso*0.2
    print("Se voce Não fazer seu Cardio Vai virar a Thais Carla",peso_perdido)
elif imc>=35 and imc<=39.9:
    peso_perdido=peso*0.3
    print("Ta se Transformando nela, vo te come vo te come",peso_perdido)
else:
    peso_perdido=peso*0.4
    print("Viro a Thais Carla Pique Majin Boo",peso_perdido)

    
