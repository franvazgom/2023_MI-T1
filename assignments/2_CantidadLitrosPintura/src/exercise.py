def main():
    #escribe tu código abajo de esta línea
    
    areaPintura = float(input("ingrese el area de la superficie que desea pintar: "))
    litroPintura = float(input("Ingrese los litros de pintura: "))

    rendimiento = int(areaPintura/litroPintura)

    print(rendimiento)

if __name__ == '__main__':
    main()
