# ---------------------EJERCICIO1-------------------------
def maximo_comun_divisor(a, b):
    temporal = 0
    while b != 0:
        temporal = b
        b = a % b
        a = temporal
    return a

# ---------------------EJERCICIO2-------------------------
def minimo_comun_multiplo(a, b):
    return (a * b) / maximo_comun_divisor(a, b)


a = 20
b = 6
mcm = minimo_comun_multiplo(a, b)
print(f"El mínimo común múltiplo de {a} y {b} es {mcm}")

# ---------------------EJERCICIO3 Y 4-------------------------
def creador_dict(cadena):
# Recibe una cadena de caracteres y regresa un diccionario con las palabras (keys) y conteo (value)
    list_1= cadena.split()
    dict_1={}
    
    for i in list_1:
        if i in dict_1:
            dict_1[i] +=1
        else:
            dict_1[i]= 1
    return dict_1

def contador_dict(dictionario):
'''Recibe un diccionario y regresa una tupla: la palabra mas repetida y cuantas veces aparece'''
    palabra_frecuente= ''
    cantidad=0
    for keys,values in dictionario.items():
        if values > cantidad:
            cantidad= values
            palabra_frecuente= keys
    
    return palabra_frecuente,cantidad

entrada=input('Ingrese su cadena de caracteres: ')
print(creador_dict(entrada))
print(contador_dict(creador_dict(entrada)))

# ---------------------EJERCICIO 5-------------------------
def get_int_recu(): #recursiva
    user_input = input('Ingrese un numero int: ')
    try:
        value = int(user_input)
    except ValueError:
        print('No es int. Otro!!!')
        return get_int()
    else:
        return value

def get_int_itera():
    while True:
        user_input = input('Give me an integer number: ')
        try:
            value = int(user_input)
        except ValueError:
            print('Not a valid integer. Try it again!')
        else:
            return value


# ---------------------EJERCICIO 6-------------------------