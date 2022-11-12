import random 



def  run():
    nuemero_aleatoreo =random.randint(1, 100)
    numero_elegido = int (input ("elige un numero del 1 al 100:"))
    while numero_elegido != nuemero_aleatoreo:
        if numero_elegido < nuemero_aleatoreo:
            print("busca un mumero mas grande ")
        else:
            print("Busca un numero mas menor ")
        numero_elegido =int(input("elije otro numero:  "))


    print ("ganaste")


if __name__ == "__main__":
    run()