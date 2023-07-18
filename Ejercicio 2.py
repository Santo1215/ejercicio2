import random

class Cartas:
    def __init__(self, palo, valor):
        self.palo = palo
        self.valor = valor

    def __str__(self):
        return f"{self.valor} de {self.palo}"


class Mazo:
    def __init__(self):
        self.cartas = []
        palos = ["♥️", "♦️", "♣️", "♠️"]
        valores = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "As"]

        for palo in palos:
            for valor in valores:
                self.cartas.append(Cartas(palo, valor))

        random.shuffle(self.cartas)

    def repartir_carta(self):
        return self.cartas.pop()

class Mano:
    def __init__(self):
        self.cartas = []
        self.valor = 0

    def agregar_carta(self, carta):
        self.cartas.append(carta)
        self.calcular_valor()

    def calcular_valor(self):
        self.valor = 0
        cuenta_ases = 0

        for carta in self.cartas:
            if carta.valor.isdigit():
                self.valor += int(carta.valor)
            elif carta.valor in ["J", "Q", "K"]:
                self.valor += 10
            elif carta.valor == "As":
                cuenta_ases += 1

        for _ in range(cuenta_ases):
            if self.valor + 11 <= 21:
                self.valor += 11
            else:
                self.valor += 1

class Jugador:
    def __init__(self, nombre):
        self.nombre = nombre
        self.mano = Mano()

    def __str__(self):
        return f"Cartas del {self.nombre}: {', '.join(str(carta) for carta in self.mano.cartas)}"
class Blackjack:
    def __init__(self):
        self.mazo = Mazo()
        self.Jugador = Jugador("Jugador")
        self.dealer = Jugador("Dealer")
        self.apuesta = 0

    def repartir_cartas_iniciales(self):
        for _ in range(2):
            self.Jugador.mano.agregar_carta(self.mazo.repartir_carta())
            self.dealer.mano.agregar_carta(self.mazo.repartir_carta())

    def turno_jugador(self):
        elegir = None
        while True:
            print(self.Jugador)
            if elegir == None:
                self.apuesta = int(input("Ingresa tu apuesta: "))
            elif elegir == "si" or elegir == "Si" or elegir == "SI" or elegir == "sI":
                elegirapuesta = input("Quieres mantener o subir la apuesta? (mantener/subir): ")
                if elegirapuesta == "subir":
                    self.apuesta += int(input("Cuanto quieres subir la apuesta?: "))
                else:
                    print("Opción no valida. Prueba otra vez")
                    return elegirapuesta
            
            elegir = input("Quieres otra? (si/no): ").lower()
            if elegir == "si" or elegir == "Si" or elegir == "SI" or elegir == "sI":
                self.Jugador.mano.agregar_carta(self.mazo.repartir_carta())
                
                if self.Jugador.mano.valor > 21:
                    print(f"{self.Jugador} = {self.Jugador.mano.valor}")
                    print("Te pasaste! el Dealer gana.")
                    print(f"Perdiste {self.apuesta}")
                    return False
            elif elegir == "no" or elegir == "NO" or elegir == "No" or elegir == "nO":
                return True
            else:
                print("Opción no valida. Prueba otra vez.")
                return elegir

    def turno_dealer(self):
        while self.dealer.mano.valor < 17:
            self.dealer.mano.agregar_carta(self.mazo.repartir_carta())

        print(self.dealer)
        if self.dealer.mano.valor > 21:
            print("Dealer se pasó! Tú ganas.")
            print(f"Obtienes {self.apuesta*2}")
        elif self.dealer.mano.valor >= self.Jugador.mano.valor:
            print(f"= {self.dealer.mano.valor}")
            print("El Dealer gana.")
            print(f"Perdiste {self.apuesta}")
        else:
            print("Tú ganas!")
            print(f"Obtienes {self.apuesta*2}")

    def jugar(self):
        print("Bienvenido a Blackjack!")
        self.repartir_cartas_iniciales()
        if self.turno_jugador():
            self.turno_dealer()

if __name__ == "__main__":
    Juego = Blackjack()
    Juego.jugar()