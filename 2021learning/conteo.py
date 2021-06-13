frase = "Hoy ha salido el sol y hace una mañana estupenda."
conteo = {}

for letra in frase.lower():
    if letra not in conteo:
        conteo[letra]=1
    else:
        conteo[letra]+=1

for k, v in conteo.items():
    print(f"{k}: {v}")
