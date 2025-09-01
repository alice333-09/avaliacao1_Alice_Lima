peso= float(input("digite seu peso em KG: "))
altura=float(input("digite sua altura em metros: ")) 
IMC= peso/(altura * altura)
print(IMC)
if IMC < 18.5:
    print("Abaixo do peso")
if 18.5 <= IMC < 25:
    print("Peso normal")
if 25 <= IMC < 30:
    print("Sobrepeso")
elif IMC >= 30:
    print("obesidade")
