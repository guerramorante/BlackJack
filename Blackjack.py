import random 
cartas_dealer = []
cartas_jugador = []
while len(cartas_dealer) != 2:
    cartas_dealer.append(random.randint(1,11))
    if len(cartas_dealer) == 2:
        print("El dealer tiene: X &", cartas_dealer[1])

while len(cartas_jugador) != 2:
    cartas_jugador.append(random.randint(1,11))
    if len(cartas_jugador) == 2:
        print("Usted tiene: ", cartas_jugador)        
         
if sum(cartas_dealer) == 21:
    print("Total 21 gana el dealer")
elif sum(cartas_dealer) > 21:
    print("El dealer pierde")

while sum(cartas_jugador) < 21:
    medidas_adoptadas = str(input("¿Desea pedir una carta o plantarse?  "))
    if medidas_adoptadas == "hit":
        cartas_jugador.append(random.randint(1,11))
        print("Ahora tiene un total de " + str(sum(cartas_jugador)) + " de estas cartas ", cartas_jugador)
    else:
        print("El dealer tiene un total de " + str(sum(cartas_dealer)) + " with ", cartas_dealer)
        print("Usted tiene un total de " + str(sum(cartas_jugador)) + " with ", cartas_jugador)
        if sum(cartas_dealer) > sum(cartas_jugador):
            print("El dealer gana")
        else:
            print("¡Ha ganado!")
            break
if sum(cartas_jugador) > 21:
    print("Perdiste, el dealer gana")
elif sum(cartas_jugador) == 21:
    print("BlackJack, ¡ganador!")       