def jugar(intento=1):
    respuesta = input("¿De que color es la fruta?: \n")
    if respuesta != ("Roja" or "roja"):
        if intento < 3 : 
            print("\nFallaste, intentalo otra vez")
            intento += 1
            jugar(intento)
        else:
            print("\nPerdiste :(")
    else:
        print("\n¡Ganaste!")
        
jugar()