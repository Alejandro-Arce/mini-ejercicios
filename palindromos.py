def palindromo (palabra):

    palabra = palabra.replace(' ', '')
    palabra = palabra.lower ()
    palabra_invertida = palabra_invertida [::-1]
    
    
    if palabra ==palabra_invertida:
        return True
    
    
    else:
        return False
        
        
def run():

    palabra = input("escriba una palabra: ") 
    es_palindromo = palindromo(palabra)
    if es_palindromo == True :
        print("es palindromo ")
    else :
        print("no palindromo ")



if  __name__ == '__main__':
    run()