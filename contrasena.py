import random

def generar_consasena():
    
    mayusculas = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    minusculas = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    simbolos   = ["_", "-", "=", "+", ":", ";", "'", ">","<", "?",]
    numeros    = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]

    caracteres  = mayusculas + minusculas + numeros + simbolos

    contrasena = []

    for i in range (15):
        caracter_random = random.choice(caracteres)
        contrasena.append(caracter_random) 

    contrasena = "".join(contrasena)
    
    return contrasena 

def run():
    contrasena = generar_consasena()
    print( "tu nueva contrasena es : " + contrasena)





if __name__ == "__main__":
    run()