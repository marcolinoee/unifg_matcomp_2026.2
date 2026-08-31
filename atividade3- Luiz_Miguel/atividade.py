import time
import random

carros = "VERMELHO"
pedestres = "VERMELHO"
cancela = "ABERTA"

while True:
    evento = random.choice(["normal", "pedestre", "ambulancia", "trem"])

    print("\n----------------------------")

    if evento == "trem":
        carros = pedestres = "VERMELHO"
        cancela = "FECHADA"

        print("🚆 TREM DETECTADO")
        print("🚧 CANCELA FECHADA")
        print("🛑 TUDO PARADO")
        time.sleep(5)

        cancela = "ABERTA"
        print("🚧 CANCELA ABERTA")

    elif evento == "ambulancia":
        carros = "VERDE"
        pedestres = "VERMELHO"

        print("🚑 AMBULÂNCIA DETECTADA")
        print("🚗 SEMÁFORO: VERDE")
        print("🚶 PEDESTRES: PARADOS")
        time.sleep(4)

    elif evento == "pedestre":
        carros = "VERMELHO"
        pedestres = "VERDE"

        print("🚶 PEDESTRE DETECTADO")
        print("🚗 VEÍCULOS: PARADOS")
        print("🚶 PEDESTRES: VERDE")
        time.sleep(4)

    else:
        carros = "VERDE"
        pedestres = "VERMELHO"

        print("🚗 TRÂNSITO NORMAL")
        print("🚦 VEÍCULOS: VERDE")
        print("🚶 PEDESTRES: PARADOS")
        time.sleep(4)