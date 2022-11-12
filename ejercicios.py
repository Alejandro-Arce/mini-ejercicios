

#def funcion_max (n1,n2) :
#    if n1>n2 :
#        return n1 
#    else :
#        return n2
#
#print(funcion_max (-198,3))


#def fu_max_tres (n1,n2,n3):
#    if n1>n2 and n1>n3: 
#        return n1
#    elif n3>n2 and n3>n1:
#        return n3
#    else :
#        return n2
#
#
#print(fu_max_tres(-1,2,5))

def si_vocol(caracter):
    lista_vocales= ["a","e","i","o","u","A","E","I","O","U",]
    if caracter in lista_vocales:
        return True
    else:
        return False

print (si_vocol ("I") )