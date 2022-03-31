height = float(input("Coloque sua altura em cm: "))
weight = float(input("Coloque seu peso em Kg: "))

IMC = weight / (height/100)**2

print("Seu indice de gordura corporal é180", IMC)

if IMC <= 18.5:
    print("Você é meio mamgro(a).")
elif IMC <= 24.9:
    print("É, peso saldavel")
elif IMC <= 29.9:
    print("Vc devia perder um pouco de gordura")
else:
    print("Toma cuidado, se você cair, vai ser muito difícil se levantar.")
