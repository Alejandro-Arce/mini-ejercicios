def  run():



#    for contador in range(10000):
#        if contador %2  ≠  0:
#            continue
#        print (contador)



#    for i in range(10000):
#        if i ==5000:
#            break


    texto = input ("escribe un texto: ")
    for letra in texto: 
        if letra == "o":
            break
        print (letra)

if __name__ == "__main__":
    run()