
def mostrar_estado(e, oro, mochila): 
    print(f"\n[ ENERGÍA: {'■' * e}{'□' * (5-e)} ({e}/5) ]")
    print(f"[ ORO: {oro} | INVENTARIO: {mochila} ]")

def caminar(e, o): 
    if e > 0:
        print(">> Caminas por el bosque...")
        monedas_encontradas = random.randint(5, 15)
        print(f">> ¡Encontraste {monedas_encontradas} monedas de oro!")
        return e - 1, o + monedas_encontradas
    return e, o

def descansar(e):
    if e < 5:
        print(">> Descansas un rato y recuperas fuerzas.")
        return e + 1
    print(">> Ya estás totalmente descansado.")
    return e

def encontrar_item(mochila):
    suerte = random.randint(1, 10)
    if suerte <= 3: 
        print(">> ¡Has encontrado una Poción de Energía!")
        mochila.append("Poción")

import random 

def encuentro_enemigo(e):    
    suerte = random.randint(1, 10)
    
    if suerte <= 3: 
        print("\n¡CUIDADO! Un duende salvaje apareció.")
        opcion = input("¿Pelear o Escapar? (p/e): ").lower()
        
        if opcion == "p":
            print("¡Le diste una patada! Pero te cansaste mucho.")
            return e - 2
        else:
            print("Escapaste por poco...")
            return e - 1
    return e

energia = 3
oro = 0
inventario = [] 

while energia > 0:
    mostrar_estado(energia, oro, inventario)
    accion = input("¿Qué quieres hacer? (caminar/descansar/curar/salir): ").lower()
    
    if accion == "caminar":
        energia, oro = caminar(energia, oro) 
        energia = encuentro_enemigo(energia)
        encontrar_item(inventario)
        if energia < 0:
            energia = 0
    elif accion == "descansar":
        energia = descansar(energia)
    elif accion == "curar":
        if "Poción" in inventario: 
            print(">> Bebes una poción y recuperas 2 de energía.")
            inventario.remove("Poción")
            energia = energia + 2
            if energia > 5: 
                energia = 5
        else:
            print(">> No tienes pociones en el inventario.")    
    elif accion == "salir":
        print("Saliendo del juego...")
        break 
    else:
        print("Comando no válido.")
    if oro >= 100:
        print("\n" + "*"*30)
        print("¡FELICIDADES! Has recolectado 100 monedas y has comprado tu libertad.")
        print("HAS GANADO EL JUEGO.")
        print("*"*30)
        break 

print("\n--- JUEGO TERMINADO ---")