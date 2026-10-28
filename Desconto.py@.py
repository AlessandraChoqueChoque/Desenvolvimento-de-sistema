valor=(float(input("digite o valor")))
if valor>=500:
    desconto=valor*0.20
    valorcomdesconto=valor-desconto
    print(valorcomdesconto)
elif valor>=200:
    desconto=valor*0.10
    valorcomdesconto=valor-desconto
    print(valorcomdesconto)
else:
    print("sem desconto")