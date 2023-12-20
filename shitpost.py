file.open('datorium.txt')
while True:
    eur  = int(input("Ievadie eur  "))
    with open("datorium.txt", "r" , encoding="utf-8") as f:
        a = float(f.read())
        gb = eur*a
        print(f"{eur}EUR = {gb}GBP")