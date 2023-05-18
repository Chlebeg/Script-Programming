if __name__ == "__main__":
    lancuch1 = "Ala ma kota\nKot ma Ale"
    lancuch2 = "Tadeusz ma psa\nPies nie ma tadeusza"

    print(((lancuch1 + " " + lancuch2)*3).replace("\n", " "))

    lancuch = "Litwo! Ojczyzno moja! ty jestes jak zdrowie. Ile cie trzeba cenic, ten tylko sie dowie, Kto cie stracil."

    print(lancuch[0])
    print(lancuch[0:2])
    print(lancuch[2:])
    print(lancuch[-1])
    print(lancuch[-3:])
    print(lancuch[1::2])
